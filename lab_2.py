def readFile(name):
    try:
        with open(name, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File '{name}' not found.")
        return []

def merge(news1, news2):
    merged_news = []
    max_length = max(len(news1), len(news2))

    for i in range(max_length):
        if i < len(news1):
            merged_news.append(news1[i].strip())

        if i < len(news2):
            merged_news.append(news2[i].strip())

    return merged_news

def saveMerged(merged_news):
    with open("news.txt", "w") as file:
        for line in merged_news:
            file.write(line + "\n")


file1 = input("Enter the file name of the javaScript: ")
file2 = input("Enter the file name of the node js: ")

news1 = readFile(file1)
news2 = readFile(file2)

merged_news = merge(news1, news2)

for line in merged_news:
    print(line)

saveMerged(merged_news)


