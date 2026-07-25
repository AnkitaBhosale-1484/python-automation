'''Write a program that scans a specified directory every minute.
The task should display:
• Directory name
• Number of files
• Number of subdirectories
• Date and time of scanning
Use the os module.
Example Output:
Directory Scanned : E:/Data
Total Files : 15
Total Subdirectories : 4
Scan Time : 25-07-2026 04:30:00 PM'''



import os
import schedule
import time
import datetime

def GetDirectory():
    Directory = input("Enter Directory Path : ")
    return Directory

def ScanDirectory(Directory):

    FileCount = 0
    DirectoryCount = 0

    for FolderName, SubFolder, FileName in os.walk(Directory):

        FileCount = FileCount + len(FileName)
        DirectoryCount = DirectoryCount + len(SubFolder)

    print("Directory Scanned :", Directory)
    print("Total Files :", FileCount)
    print("Total Subdirectories :", DirectoryCount)
    print("Scan Time :", datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    print("--------------------------------")

def main():

    Directory = GetDirectory()

    schedule.every().minute.do(ScanDirectory, Directory)

    print("Directory Scanner Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()