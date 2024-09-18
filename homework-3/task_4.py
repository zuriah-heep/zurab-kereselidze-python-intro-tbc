from random import randrange

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']

random_suit = randrange(len(suits))
random_rank = randrange(len(ranks))

print(ranks[random_rank], 'of', suits[random_suit])