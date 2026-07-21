'''Display file contents
write a program which accept  a file name from the user ,opens that file,and display the entire contents on the console
input Demo.txt
output  display content of Demo.txt on console'''

def main():
    filename=input("enter the filename:")
    f=open(filename,"r")
    data=f.read()
    print("content of file:",filename)
    print(data)

if __name__=="__main__":
    main()