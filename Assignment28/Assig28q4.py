'''Copy File Contents into Another File
Write a program which accepts two file names from the user.
First file is an existing file.
Second file is a new file.
Copy all contents from the first file into the second file.
Input:
Demo.txt
ABC.txt
Expected Output:
Contents of Demo.txt copied into Abc.txt.'''

def main():
    try:
        existingfile=input("enter the existing file name:")
        f1=open(existingfile,"r")
        data=f1.read()

        newfile=input("enter new  file name:")
        f2=open(newfile,"w")
        f2.write(data)

        print("Contents of", existingfile, "copied into", newfile)
        

        f1.close()
        f2.close()

    except FileNotFoundError:
        print("file not found")

if __name__=="__main__":
    main()

        