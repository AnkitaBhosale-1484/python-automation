'''Write a program that copies all .txt files from one directory to another every ten minutes.
The program should:
Accept Source Directory
Accept Destination Directory
Validate both directories
Copy only .txt files
Maintain a log of copied files
Do not stop if one file cannot be copied'''

import os
import shutil
import schedule
import time
import datetime

def GetSourceDirectory():
    Source = input("Enter Source Directory : ")
    return Source

def GetDestinationDirectory():
    Destination = input("Enter Destination Directory : ")
    return Destination

def CopyTextFiles(Source, Destination):

    if os.path.isdir(Source) == False:
        print("Source directory does not exist.")
        return

    if os.path.isdir(Destination) == False:
        print("Destination directory does not exist.")
        return

    f = open("CopyLog.txt", "a")

    for FolderName, SubFolder, FileName in os.walk(Source):

        for fname in FileName:

            if fname.endswith(".txt"):

                SourcePath = os.path.join(FolderName, fname)

                try:
                    shutil.copy(SourcePath, Destination)

                    f.write("Copied : " + SourcePath + "\n")
                    f.write("Date and Time : ")
                    f.write(datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
                    f.write("\n")
                    f.write("-"*40)
                    f.write("\n")

                    print(fname, "Copied Successfully")

                except Exception:
                    print(fname, "Could not be copied.")

    f.close()

def main():

    Source = GetSourceDirectory()
    Destination = GetDestinationDirectory()

    schedule.every(10).minutes.do(CopyTextFiles, Source, Destination)

    print("Copy Scheduler Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()