'''Write a program that accepts:
• A message from the user
• A time interval in seconds
Schedule the program to display the message repeatedly after the specified interval.
Example Input:
Enter message: Jay Ganesh
Enter interval in seconds: 5
Expected Output:
Jay Ganesh
every five seconds.
Validate that the interval is greater than zero.'''

import time
import schedule
def Message():
    message=input("Enter message:")
    return message

def Interval():
    interval=int(input("enter interval in seconds:"))
    return interval



def DisplayMessage(message):
    print(message)

def main():
    MessageData=Message()
    IntervalData=Interval()
    if IntervalData <= 0:
        print("Interval should be greater than zero.")
        return
    
    schedule.every(IntervalData).seconds.do(DisplayMessage,MessageData)
   

    while True:
        schedule.run_pending()
        time.sleep(1)




if __name__=="__main__":
    main()
    