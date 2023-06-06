def calculateHarrisBenedict(weight, height, age, gender):
    if gender == "male":
        bmr = 66.5 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
    elif gender == "female":
        bmr = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
    else:
        raise ValueError("Invalid gender. Please enter 'male' or 'female'.")
    return bmr


weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))
age = int(input("Enter your age: "))
gender = input("Enter your gender (male/female): ")

bmr = calculateHarrisBenedict(weight, height, age, gender)

print("Your basic metabolism: ", bmr)
