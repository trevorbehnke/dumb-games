raw_list = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

suit_hearts = []
suit_spades = []
suit_diamonds = []
suit_clubs = []

hearts = 'Hearts'
for card in raw_list:
    suit_hearts.append(hearts)

hearts = zip(raw_list, suit_hearts)

spades = 'Spades'
for card in raw_list:
    suit_spades.append(spades)

spades = zip(raw_list, suit_spades)

diamonds = 'Diamonds'
for card in raw_list:
    suit_diamonds.append(diamonds)

diamonds = zip(raw_list, suit_diamonds)

clubs = 'Clubs'
for card in raw_list:
    suit_clubs.append(clubs)

clubs = zip(raw_list, suit_clubs)

deck = [tuple(hearts), tuple(spades), tuple(diamonds), tuple(clubs)]

# print(tuple(hearts))
# print(tuple(spades))
# print(tuple(diamonds))
# print(tuple(clubs))

print(deck)