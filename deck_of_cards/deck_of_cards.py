"""
design a deck of cards:

A deck is a list of card all stacked together. Represent Card as an object and create a list of cards
for each different color i.e spades, club, hearts, diamond
"""
import random

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        return 'Card(value=' + str(self.value) + ', color=' + str(self.color) + ')'

colors = ['Spade', 'Club', 'Hearts', 'Diamond']
class Deck:
    def __init__(self):
        self.deck = [Card(value, color) for value in range(1, 14) for color in colors]

    def play(self):
        return self.deck.pop(0)

if __name__ == "__main__":
    cdeck = Deck()
    deck = cdeck.deck
    print(len(deck))
    cdeck.play()
    print(len(deck))
