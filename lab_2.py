class Beer:
    def __init__(self, name, category, alcohol_percentage, price, rating):
        self.name = name
        self.category = category
        self.alcohol_percentage = alcohol_percentage
        self.price = price
        self.rating = rating

class Store:
    def __init__(self):
        self.beers = []

    def add_beer(self, beer):
        self.beers.append(beer)

    def sort_by_rating(self):
        self.beers.sort(key=lambda beer: beer.rating, reverse=True)

    def sort_by_name(self):
        self.beers.sort(key=lambda beer: beer.name)

    def display_beers(self):
        for beer in self.beers:
            print(f"Name: {beer.name}")
            print(f"Category: {beer.category}")
            print(f"Alcohol Percentage: {beer.alcohol_percentage}")
            print(f"Price: {beer.price}")
            print(f"Rating: {beer.rating}")
            print("---------------------")


beer1 = Beer("IPA", "India Pale Ale", 6.5, 3.99, 4.3)
beer2 = Beer("Stout", "Stout", 5.8, 4.99, 4.1)
beer3 = Beer("Pilsner", "Pilsner", 4.8, 2.99, 4.5)

store = Store()

store.add_beer(beer1)
store.add_beer(beer2)
store.add_beer(beer3)

store.sort_by_rating()

store.display_beers()
