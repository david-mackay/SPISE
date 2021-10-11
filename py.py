# import random
# class Card(object):
#     def __init__(self, face, suit):
#         self.face = face
#         self.suit = suit
#         if face == 'J':
#             self.value = 11
#         elif face == 'Q':
#             self.value = 12
#         elif face == 'K':
#             self.value = 13
#         elif face == 'A':
#             self.value = 14
#         else:
#             self.value = int(face)
#     def __str__(self):
#         return str(self.face)+str(self.suit)

# cards = [str(i) for i in range(2,11)]
# cards += ['J', 'Q', 'K', 'A']

# suits = ['h','s','d','c']
# deck =[]
# for suit in suits:
#     for card in cards:
#         deck.append(Card(card,suit))

# random.shuffle(deck)

# class Player(object):
#     def __init__(self, name):
#         self.name = name
#         self.hand = []
    
#     def add_card(self, card):
#         self.hand.append(card)

#     def find_winner(self, other):
#         player_total = 0
#         for card in self.hand:
#             player_total += card.value
#         other_total = 0
#         for card in other.hand:
#             other_total += card.value

#         return other if other_total>player_total else self
    
#     def __str__(self):
#         return self.name


# player1 = Player('David')
# player2 = Player('Kyle')

# number_of_cards_per_player = 4

# for num in range(number_of_cards_per_player):
#     player1.add_card(deck.pop(0))
#     player2.add_card(deck.pop(0))

# for card in player1.hand:
#     print(card,player1.name)
# for card in player2.hand:
#     print(card,player2.name)

# print(player1.find_winner(player2))



deal = [['Ah', 'Ac'], ['Kd','Jh']]

hands ={}
for i in range(len(deal)):
    hands['player' + str(i+1)] = deal[i]

print(hands)