class Auto:
    name = ""
    model = ""
    mileage = ""
    color = ""
    size = ""

    def __init__(self, name, model, mileage, color, size):
        self.name = name
        self.model = model
        self.mileage = mileage
        self.color = color
        self.size = size

    def goStraight(self):
        print("Name: " + str(self.name))
        print("Model: " + str(self.model))
        print("Mileage:" + str(self.mileage))

    def oldAuto(self):
        print("Old auto: " + str(self.mileage))

    def populateModel(self):
        print("Populate Model: " + str(self.name) + " " + self.model)

    def newAuto(self):
        print("New auto: " + str(self.name) + " Model: " + self.model + " Mileage: " + str(self.mileage))


obj1 = Auto("BMW", "X", 60000, "red", "big")
obj2 = Auto("Audi", "MZ", 54263, "black", "small")
obj3 = Auto("Citroen", "C3", 563, "Green", "big")
obj1.goStraight()
obj2.goStraight()
obj1.populateModel()
obj3.newAuto()
