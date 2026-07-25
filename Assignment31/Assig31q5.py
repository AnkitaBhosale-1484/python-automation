'''Write a program that accepts a directory name from the user and counts the number of files inside it every five minutes.
Write the result into:
DirectoryCountLog.txt
Each entry should contain:
Directory path
Number of files
Date and time'''

import os
import schedule
import time
import datetime

def GetDirectory():
    Directory = input("Enter Directory Path : ")
    return Directory

def CountFiles(Directory):

    TotalFiles = 0

    for FolderName, SubFolder, FileName in os.walk(Directory):
        TotalFiles = TotalFiles + len(FileName)

    f = open("DirectoryCountLog.txt","a")

    f.write("Directory Path : " + Directory + "\n")
    f.write("Number of Files : " + str(TotalFiles) + "\n")
    f.write("Date and Time : ")
    f.write(datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    f.write("\n")
    f.write("-"*40)
    f.write("\n")

    f.close()

    print("Directory :", Directory)
    print("Number of Files :", TotalFiles)
    print()

def main():

    Directory = GetDirectory()

    schedule.every(2).seconds.do(CountFiles, Directory)

    print("Directory Scanner Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()