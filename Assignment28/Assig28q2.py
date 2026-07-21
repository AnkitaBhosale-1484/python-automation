'''count words in a file 
write a program which accept a file  name from the user and counts the total number of words in that file
input demo.txt output total number of words in demo.txt'''

def main():
    try:
        filename=input("enter the filename:")
        f=open(filename,"r")

        data=f.read()
        words=data.split()
        print("total number words in demo.txt:",len(words))

        f.close()



    except FileNotFoundError:
        print("file not found")


    
if __name__=="__main__":
    main()