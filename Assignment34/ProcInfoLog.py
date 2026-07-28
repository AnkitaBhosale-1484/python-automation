'''Design automation script which accept directory name from user and create log file in that directory which contains information of running processes as its name, PID, Username.
Usage:
python ProcInfoLog.py Demo
Demo = Directory Name

Design automation script which accept directory name and mail id from user and create log file in that directory which contains information of running processes as its name, PID, Username. After creating log file send that log file to the specified mail.
Usage
python ProcInfoLog.py Demo abc@gmail.com

'''

import psutil
import sys
import os
import time
from SendMail import SendMail

def DisplayProcess():
    try:
        ProcessList=[]

        for process in psutil.process_iter(["pid","name","username"]):
            ProcessList.append(process.info)

    except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            print("Unable to access process")
    

    return ProcessList

def CreateDirectory(DirectoryName):
    if  not os.path.exists(DirectoryName):
        os.mkdir(DirectoryName)

    return True

def CreateLogFile(DirectoryName):
    timestamp=time.strftime("%Y_%m_%d_%H_%M_%S_%p")
    FileName=os.path.join(DirectoryName,"ProcessLog_%s.log" % timestamp)

    return FileName





def main():
    if len(sys.argv)!=3:
        print("uasage:python ProcInfoLog.py DirectoryName EmailId")
        return

    DirectoryName = sys.argv[1]
    Receiver = sys.argv[2]


    DirectoryName=sys.argv[1]
    CreateDirectory(DirectoryName)

    FileName=CreateLogFile(DirectoryName)

    Data=DisplayProcess()

    Border = "-" * 50

    fobj = open(FileName, "w")

    fobj.write(Border + "\n")
    fobj.write("Running Process Information\n")
    fobj.write("Log Created At : " + time.ctime() + "\n")
    fobj.write(Border + "\n\n")

    for value in Data:

        fobj.write("PID : %s\n" % value["pid"])
        fobj.write("Name : %s\n" % value["name"])
        fobj.write("UserName : %s\n" % value["username"])
        fobj.write(Border + "\n")

    fobj.close()

    print("Log file created successfully.")

    Subject = "Process Log Report"

    Body = "Please find attached process log file."

    SendMail(Receiver, Subject, Body, FileName)
    


if __name__=="__main__":
    main()