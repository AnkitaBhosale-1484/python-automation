'''Write a program that creates a new text file every minute.
The filename should contain the current timestamp.
Example filename:
File_25_07_2026_16_30_00.txt
Write the following information into the file:
Filename
Creation date
Creation time'''

import schedule
import time
import datetime

def CreateFile():

    CurrentTime = datetime.datetime.now()

    FileName = "File_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    f = open(FileName, "w")

    f.write("Filename : " + FileName + "\n")
    f.write("Creation Date : ")
    f.write(CurrentTime.strftime("%d-%m-%Y"))
    f.write("\n")

    f.write("Creation Time : ")
    f.write(CurrentTime.strftime("%I:%M:%S %p"))

    f.close()

    print(FileName, "created successfully.")

def main():

    schedule.every(1).minutes.do(CreateFile)

    print("File Creator Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()