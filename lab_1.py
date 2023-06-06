class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is now open.")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def display_flavors(self):
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print(flavor)

class CoffeeShop(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.coffee = []

    def add_coffee(self, coffee_type):
        self.coffee.append(coffee_type)

    def display_coffee(self):
        print("Available Coffee Types:")
        for coffee_type in self.coffee:
            print(coffee_type)


restaurant = Restaurant("Food Paradise", "Italian")
restaurant.describe_restaurant()
restaurant.open_restaurant()

ice_cream_stand = IceCreamStand("Sweet Delights", "Ice Cream")
ice_cream_stand.add_flavor("Vanilla")
ice_cream_stand.add_flavor("Chocolate")
ice_cream_stand.add_flavor("Strawberry")
ice_cream_stand.display_flavors()

coffee_shop = CoffeeShop("Caffeine Buzz", "Cafe")
coffee_shop.add_coffee("Americano")
coffee_shop.add_coffee("Latte")
coffee_shop.display_coffee()
