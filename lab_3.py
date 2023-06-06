class Citizen:
    def __init__(self, name, surname, street_number, postal_code, city):
        self.name = name
        self.surname = surname
        self.street_number = street_number
        self.postal_code = postal_code
        self.city = city

    def loadData(self, name, surname, street_number, postal_code, city):
        self.name = name
        self.surname = surname
        self.street_number = street_number
        self.postal_code = postal_code
        self.city = city

    def businessCard(self):
        print("----------------------")
        print(f"{self.name} {self.surname}")
        print(f"ул. {self.street_number}")
        print(f"{self.postal_code} {self.city}")
        print("----------------------")

    def printToFile(self, filename):
        with open(filename, "w") as file:
            file.write("----------------------\n")
            file.write(f"{self.name} {self.surname}\n")
            file.write(f"ул. {self.street_number}\n")
            file.write(f"{self.postal_code} {self.city}\n")
            file.write("----------------------\n")


citizen = Citizen("", "", "", "", "")
citizen.loadData("Tanya", "Kulinkovich", "Rakowiecka 20", "00-001", "Wroclaw")
citizen.businessCard()
citizen.printToFile("card.txt")
