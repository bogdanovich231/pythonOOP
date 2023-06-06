text = "Mr. Tadeusz, today is our last day!"
with open("pantadeus.txt", "w") as file:
    file.write(text)

with open("pantadeus.txt", "r") as file:
    content = file.read()
    print(content)

# Suggest a solution to the text readability problems
with open("pantadeus.txt", "r") as file:
    content = file.read().strip().split()
    print(content)
