'''compare two files(command Line)
write a program which accept  two file names through command line argument and compares the contents of both files
if both files contain the same contents ,display success
otherwise display Failure
input (command line)
Demo.txt Hello.txt
output Sucess or Failure'''

import sys

def main():
    try:
        file1 = sys.argv[1]
        file2 = sys.argv[2]

        f1 = open(file1, "r")
        f2 = open(file2, "r")

        data1 = f1.read()
        data2 = f2.read()

        if data1 == data2:
            print("Success")
        else:
            print("Failure")

        f1.close()
        f2.close()

    except FileNotFoundError:
        print("File not found")

    except IndexError:
        print("Please provide two file names")


if __name__ == "__main__":
    main()