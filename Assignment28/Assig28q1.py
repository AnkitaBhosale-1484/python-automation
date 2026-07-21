'''Count Lines in a File
Problem Statement:
Write a pougnan which accopts a file name on the user  and counts how many lines are present in the file.
Input: Demo-txt
Expected Output:
Total nummber of lines in Demo.txt'''


def main():
    try:
        filename=input("enter the filename:")
        f=open(filename,"r")

        count=0
        for lines in f:
            count += 1
        print("lines present in the file",count)

    except FileNotFoundError:
        print("file not found")



if __name__=="__main__":
    main()