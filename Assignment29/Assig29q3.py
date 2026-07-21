'''copy file content into a new file(command line)
write a program which accept an existing file name through command line argument,creats a new file named Demo.txt and copies all contents from the given file into Demo.txt
input (command Line)Abc.txt
output create Demo.txt and copies all Abc.txt into Demo.txt'''
import sys
def main():
    try:
        existingfile=sys.argv[1]
        f1=open(existingfile,"r")
        data=f1.read()
        print(data)
       
        
        f2=open("Demo.txt","w")
        f2.write(data)
        print("content of ",existingfile,"copied into Demo.txt")
        f1.close()
        f2.close()



    except FileNotFoundError:
        print("file not found")





if __name__=="__main__":
    main()
