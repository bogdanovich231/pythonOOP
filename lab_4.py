import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.rank < other.rank


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def display(self):
        for card in self.cards:
            print(card)

    def move_card(self, card, destination_deck):
        if card in self.cards:
            self.cards.remove(card)
            destination_deck.add_card(card)


deck = Deck()

deck.add_card(Card("Ace", "Spades"))
deck.add_card(Card("King", "Hearts"))
deck.add_card(Card("Queen", "Diamonds"))
deck.add_card(Card("Jack", "Clubs"))

deck.display()
deck.shuffle()
print("Shuffled deck:")
deck.display()
deck.sort()
print("Sorted deck:")
deck.display()
second_deck = Deck()

card_to_move = deck.cards[0]
deck.move_card(card_to_move, second_deck)

print("First deck:")
deck.display()
print("Second deck:")
second_deck.display()
