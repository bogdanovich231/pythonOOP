import re

def checkPolishCode(postal_code):
    pattern = r'^\d{2}-\d{3}$'

    if re.match(pattern, postal_code):
        return True
    else:
        raise ValueError("Invalid Polish postal code")

def savePostalCode(postal_code):
    with open("postal_code.txt", "a") as file:
        file.write("Code: " + postal_code + "\n")

try:
    user_input = input("Enter Poland postal code: ")
    if checkPolishCode(user_input):
        savePostalCode(user_input)
        print("The postal code has been added to the file.")
except ValueError as e:
    print(e)
