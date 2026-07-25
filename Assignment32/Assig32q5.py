'''Write a program that deletes all empty files from a specified directory every hour.
The program should:
Scan the directory recursively
Detect files whose size is 0 bytes
Delete the empty files
Store deleted file paths in a log file
Handle PermissionError
Test only on a sample directory.'''

import os
import schedule
import time
import datetime

def GetDirectory():
    Directory = input("Enter Directory Path : ")
    return Directory

def DeleteEmptyFiles(Directory):

    if os.path.isdir(Directory) == False:
        print("Directory does not exist.")
        return

    f = open("DeleteLog.txt", "a")

    for FolderName, SubFolder, FileName in os.walk(Directory):

        for fname in FileName:

            FilePath = os.path.join(FolderName, fname)

            try:

                if os.path.getsize(FilePath) == 0:

                    os.remove(FilePath)

                    f.write("Deleted File : " + FilePath + "\n")
                    f.write("Date and Time : ")
                    f.write(datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
                    f.write("\n")
                    f.write("-"*40)
                    f.write("\n")

                    print(fname, "Deleted Successfully")

            except PermissionError:
                print("Permission Denied :", FilePath)

    f.close()

def main():

    Directory = GetDirectory()

    schedule.every(1).hours.do(DeleteEmptyFiles, Directory)

    print("Empty File Deleter Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()