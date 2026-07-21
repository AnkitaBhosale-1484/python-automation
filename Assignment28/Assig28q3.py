''' display file line by line 
write a program which accept file name from the user  and display the contents of the file line by line on the screen .
input demo.txt 
output display each line of demo .txt one by one'''

def main():
    try:

        filename=input("enter the filename:")
        f=open(filename,"r")

        print("display each line of demo.txt:")

        for line in f:
            print(line)

        f.close()

    except FileNotFoundError:
        print("file not found")
    


if __name__=="__main__":
    main()