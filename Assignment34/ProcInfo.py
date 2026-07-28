'''
Design automation script which display information of running processes as its name, PID, Username.
Usage: ProcInfo.py'''


import psutil
import sys




def DisplayProcess():
    ProcessList=[]

    try:
        for process in psutil.process_iter(["pid","name","username"]):
            ProcessList.append(process.info)

    except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
        print("Unable to access process")

    return ProcessList


def SearchProcess(ProcessName):
    ProcessList=[]
    for process in psutil.process_iter(["pid","name","username"]):
        if process.info["name"]==ProcessName:
            ProcessList.append(process.info)

    return ProcessList



def main():

    if len(sys.argv)==1:
        Data=DisplayProcess()


        for value in Data:
          print("PID:",value["pid"])
          print("Name:",value["name"])
          print("UserName:",value["username"])
          print("---------------------------------------------")

    elif len(sys.argv)==2:
        ProcessName=sys.argv[1]
        Data=SearchProcess(ProcessName)

        if len(Data)==0:
            print("Process is not found")

        else:
            for value in Data:
                      
                      print("PID:",value["pid"])
                      print("Name:",value["name"])
                      print("UserName:",value["username"])
                      print("---------------------------------------------")
    else:
        print("Invalid number of arguments")

    





if __name__=="__main__":
    main()