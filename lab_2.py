def readFile(name):
    try:
        with open(name, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File '{name}' not found.")
        return []



file1 = input("Enter the file name of the javaScript: ")
file2 = input("Enter the file name of the node js: ")

news1 = readFile(file1)
news2 = readFile(file2)


