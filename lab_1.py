class Vehicle:
    def __init__(self, nr_table):
        self.nr_table = nr_table

    def startEngine(self):
        print("Engine started.")

    def stopEngine(self):
        print("Engine stopped.")

    def move(self):
        print("Vehicle is moving.")

    def __del__(self):
        print("Vehicle object deleted.")


class Car(Vehicle):
    def __init__(self, nr_table, brand):
        super().__init__(nr_table)
        self.brand = brand

    def park(self):
        print("Car is parked.")


class Motorcycle(Vehicle):
    def __init__(self, nr_table, model):
        super().__init__(nr_table)
        self.model = model  

    def wheelie(self):
        print("Motorcycle is doing a wheelie.")



car = Car("AB1234CD", "Toyota")
print("Car brand:", car.brand)
print("Number plate:", car.nr_table)


car.startEngine()
car.move()
car.park()
car.stopEngine()


motorcycle = Motorcycle("XY9876ZW", "Harley-Davidson")
print("Motorcycle model:", motorcycle.model)
print("Number plate:", motorcycle.nr_table)


motorcycle.startEngine()
motorcycle.move()
motorcycle.wheelie()
motorcycle.stopEngine()
