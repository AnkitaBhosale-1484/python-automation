'''Create a function named:
DisplayMessage(message)
Schedule the function using:
schedule.every(5).seconds.do(DisplayMessage, message)
The message should be accepted from the user.'''

import schedule
import time
def Display():
    message=input("enter the message:")
    return message

def DisplayMessage(message):
    print(message)

def main():
    Message = Display()
    schedule.every(5).seconds.do(DisplayMessage,Message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()