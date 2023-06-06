import math

class Figure:
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Square(Figure):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def calculate_area(self):
        return self.side * self.side

    def calculate_perimeter(self):
        return 4 * self.side

class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

choice = int(input("Choose a figure:\n1 - Square\n2 - Rectangle\n3 - Triangle\n4 - Circle\n5 - Rhombus\n6 - Trapeze\n"))

if choice == 1:
    side = float(input("Enter the length of the side of the square: "))
    square = Square(side)
    print("Square footage:", square.calculate_area())
    print("The perimeter of the square:", square.calculate_perimeter())

elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle = Rectangle(length, width)
    print("Rectangle footage:", rectangle.calculate_area())
    print("Perimeter of the rectangle:", rectangle.calculate_perimeter())