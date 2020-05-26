import random

raw_set = {'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'}

suit_hearts = []
suit_spades = []
suit_diamonds = []
suit_clubs = []

hearts = 'Hearts'
for card in raw_set:
    suit_hearts.append(hearts)

hearts = zip(raw_set, suit_hearts)
hearts = list(hearts)

spades = 'Spades'
for card in raw_set:
    suit_spades.append(spades)

spades = zip(raw_set, suit_spades)
spades = list(spades)

diamonds = 'Diamonds'
for card in raw_set:
    suit_diamonds.append(diamonds)

diamonds = zip(raw_set, suit_diamonds)
diamonds = list(diamonds)

clubs = 'Clubs'
for card in raw_set:
    suit_clubs.append(clubs)

clubs = zip(raw_set, suit_clubs)
clubs = list(clubs)

deck = [hearts, spades, diamonds, clubs]
# print(deck)
class Deck:

    def __init__(self):
        pass

    def create_deck(self):
        return deck

my_deck = Deck()
print(my_deck.create_deck())
print(random.shuffle(my_deck))