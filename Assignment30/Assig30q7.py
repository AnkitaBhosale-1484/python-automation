'''Write a Python program that performs a file backup every hour.
The program should:
Accept the source file path.
Accept the destination directory path.
Copy the source file to the destination directory.
Add the current date and time to the backup filename.
Write the backup operation details into backup_log.txt.
Example backup filename
Data_25_07_2026_16_30_00.txt
Example log entry
Backup completed successfully at 25-07-2026 04:30:00 PM

Note: Use the shutil module for file copying.'''

import schedule
import os
import shutil
import time
import datetime

def SourceFile():
    source=input("enter the source file path:")
    return source
    
def DestinationDirectory():
    destination=input("enter the backup destination folder path:")
    return destination

def BackupFile(source,destination):
    FileName=os.path.basename(source)
    Name,Extension=os.path.splitext(FileName)
    CurrentTime=datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    BackupfileName=Name+"_"+CurrentTime+Extension
    DestinationPath=os.path.join(destination,BackupfileName)
    shutil.copy(source,DestinationPath)

    with open("backup_log.txt","a") as file:
        file.write("Backup completed successfully at ")
        file.write(datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
        file.write("\n")




def main():

    Source=SourceFile()
    Destination=DestinationDirectory()

    schedule.every().hour.do(BackupFile, Source, Destination)
    print("Backup started..")

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__=="__main__":
    main()