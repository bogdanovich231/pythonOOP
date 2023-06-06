class Animal:
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def nameAnimal(self):
        print(f"{self.title}")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Cat")
        self.age = age

    def createCat(self):
        print(f"The cat's name is {self.name} and he is {self.age} years old.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def createDog(self):
        print(f"The dog's name is {self.name} and he is a {self.breed} breed.")

class Bird(Animal):
    def __init__(self, name, fly):
        super().__init__(name, "Bird")
        self.fly = fly

    def birdFlight(self):
        print(f"The bird has the name {self.name} flies {self.fly}.")

class Fish(Animal):
    def __init__(self, name, live):
        super().__init__(name, "Fish")
        self.live = live

    def fishLive(self):
        print(f"The fish named {self.name} lives in {self.live}.")


animal = Animal("Dont", "Generic Animal")
animal.nameAnimal()

cat = Cat("Tom", 5)
cat.createCat()

dog = Dog("Buddy", "Labrador Retriever")
dog.createDog()

bird = Bird("Tweety", "high")
bird.birdFlight()

fish = Fish("Nemo", "Ocean")
fish.fishLive()
