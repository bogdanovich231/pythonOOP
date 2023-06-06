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

with open("pantadeus.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        if line_number in [1, 8,  12, 60, 98, 104]:
            print(f"Line {line_number}: {line.strip()}")