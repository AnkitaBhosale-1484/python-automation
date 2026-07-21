'''cheack file exists in current directory
write a program which accept a file name from the user and cheack weather that file exists in the current directory or not 
input Demo.txt
output
display weather demo.txt exist or not'''


import os
def main():
    filename=input("enter the filename:")
    
    if os.path.exists(filename):
        print(filename,"file exists in the current directory")
    else:
        print(filename,"file not exists in the current directory")



if __name__=="__main__":
    main()