'''  search word in file
write a program which accepts a file name  and a word fromthe user and cheacks weather that word in present in the file or not
input Demo.txt Maharashtra
output display weather the word Maharashtra is found in Demo.txt or not '''

def main():
    try:
        filename = input("Enter the file name: ")
        word = input("Enter the word to search: ")

        f = open(filename, "r")

        data = f.read()

        if word in data:
            print("Word", word, "is found in", filename)
        else:
            print("Word", word, "is not found in", filename)

        f.close()

    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    main()