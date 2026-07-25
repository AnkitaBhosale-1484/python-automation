'''
Write a program that reads and displays the contents of a specified text file every minute.
Handle the following conditions:
File does not exist
File is empty
Permission is denied
File cannot be opened'''

import os
import schedule
import time

def GetFilePath():
    FilePath = input("Enter Text File Path : ")
    return FilePath

def ReadFile(FilePath):

    try:
        if os.path.exists(FilePath) == False:
            print("File does not exist.")
            return

        if os.path.getsize(FilePath) == 0:
            print("File is empty.")
            return

        f = open(FilePath, "r")

        print("----------------------------")
        print(f.read())
        print("----------------------------")

        f.close()

    except PermissionError:
        print("Permission is denied.")

    except OSError:
        print("File cannot be opened.")

def main():

    FilePath = GetFilePath()

    schedule.every(1).minutes.do(ReadFile, FilePath)

    print("File Reader Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()