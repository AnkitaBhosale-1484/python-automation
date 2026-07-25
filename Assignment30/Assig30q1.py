'''Write a Python program that prints:
Jay Ganesh...
every two seconds.
Use:
schedule.every(2).seconds.do(...)
Expected Output:
Jay Ganesh...
Jay Ganesh...
Jay Ganesh...'''

import schedule
def Display():
    print("Jay Ganesh...")

def main():
    schedule.every(2).seconds.do(Display)
    while True:
        schedule.run_pending()



if __name__=="__main__":
    main()