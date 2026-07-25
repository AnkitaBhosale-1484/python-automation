'''Write a Python program that monitors the size of a specified file every 30 seconds.
Write the following details into:
FileSizeLog.txt
The log should contain:
File path
File size in bytes
Date and time
Handle the situation where the file does not exist.'''

import os
import schedule
import time
import datetime

def GetFilePath():
    FilePath = input("Enter File Path : ")
    return FilePath

def CheckFileSize(FilePath):

    if os.path.exists(FilePath) == False:
        print("File does not exist.")
        return

    FileSize = os.path.getsize(FilePath)

    f = open("FileSizeLog.txt", "a")

    f.write("File Path : " + FilePath + "\n")
    f.write("File Size : " + str(FileSize) + " bytes\n")
    f.write("Date and Time : ")
    f.write(datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    f.write("\n")
    f.write("-"*40)
    f.write("\n")

    f.close()

    print("File Size :", FileSize, "bytes")

def main():

    FilePath = GetFilePath()

    schedule.every(30).seconds.do(CheckFileSize, FilePath)

    print("File Monitor Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()