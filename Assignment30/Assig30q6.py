'''Write a script that schedules the following tasks:
Print "Lunch Time!" every day at 1:00 PM.
Print "Wrap up work" every day at 6:00 PM.
Both tasks should be handled by separate functions.'''

import schedule
import time

def LunchTime():
    print("Lunch Time")



def WrapUpWork():
    print("Wrap UP Work")


def main():
    schedule.every.at("13.00").day.do(LunchTime)
    schedule.every("18.00").day.do(WrapUpWork)
    print("scheduler started..")

    while True:
        schedule.run_pending()
        time.sleep(1)




if __name__=="__main__":
    main()