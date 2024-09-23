from random import randint
players = int(input('Enter number of players: '))

if players <= 0:
    print('Please enter a natural number')

for i in range(players):
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    print(dice1, dice2)