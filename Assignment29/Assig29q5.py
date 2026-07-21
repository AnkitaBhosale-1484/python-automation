'''Frequency of a String in File
Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.
Input:
Demo.txt
Marvellous
Expected Output:
Count how many times "Marvellous" appears in Demo.txt.'''

import sys

def main():
    try:
        filename = sys.argv[1]
        string = sys.argv[2]

        f = open(filename, "r")

        data = f.read()

        count = data.count(string)

        print(string, "appears", count, "times in", filename)

        f.close()

    except FileNotFoundError:
        print("File not found")

    except IndexError:
        print("Please provide file name and string")


if __name__ == "__main__":
    main()