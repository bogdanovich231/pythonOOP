class Student:
    def __init__(self, name, index, email):
        self.name = name
        self.index = index
        self.email = email

    def person(self, item):
        print(f"{self.name} is studying {item}.")

    def work(self, company):
        print(f"{self.name} with {self.index} is working in {company} company.")

    def contact(self, phone):
        print(f"If you want to contact {self.name}, you need to call {phone} him or {self.email}.")

student1 = Student("Tatsiana", 50254, "dsw50254@student.dsw.edu.pl")
student2 = Student("Dimitry", 65234, "dsw65234@student.dsw.edu.pl")
student3 = Student("Katerina", 42635, "kulinkovich56@gmail.com")

student3.person("computer science")
student1.work("Epam")
student2.contact("+48 513 472 031")