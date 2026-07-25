'''Write a program that creates a new log file after every ten minutes.
The filename should contain the current date and time.
Example:
MarvellousLog_25_07_2026_16_30_00.txt
The file should contain:
Log file created successfully.
Creation Time : 25-07-2026 04:30:00 PM'''

import schedule
import time
import datetime

def CreateLogFile():

    CurrentTime = datetime.datetime.now()

    FileName = "MarvellousLog_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    f = open(FileName, "w")

    f.write("Log file created successfully.\n")
    f.write("Creation Time : ")
    f.write(CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))

    f.close()

    print(FileName, "created successfully.")

def main():

    schedule.every(10).minute.do(CreateLogFile)

    print("Log File Scheduler Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()