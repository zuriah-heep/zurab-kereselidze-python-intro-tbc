from random import sample

class Player:
    def __init__(self, name):
        self.name = name

    def cards(self, card_list):
        self.cardlist = card_list
        self.points = sum([card['points'] for card in card_list])

        suit_list = [card['suit'] for card in card_list]
        self.suits = max(suit_list.count(element) for element in set(suit_list))

        rank_list = [card['rank'] for card in card_list]
        self.ranks = max(rank_list.count(element) for element in set(rank_list))

    def changecard(self, position):
        card = sample(current_deck, 1)[0]
        self.cardlist[position - 1] = card
        current_deck.remove(card)

    def display(self):
        print(f"{self.name} - {' '.join(f"{i['suit']}{i['rank']}" for i in self.cardlist)}, {self.points} points")

def deal():
    current_deck.clear()
    current_deck.extend(full_deck)
    for player in players:
        selected_cards = sample(current_deck, 5)
        player.cards(selected_cards)
        for element in selected_cards:
            current_deck.remove(element)

def remove_loser():
    min_value = min([player.points for player in players])
    similar_points_candidates = [i for i in players if i.points == min_value]
    tie = True
    if len(similar_points_candidates) == 1:
        players.remove(similar_points_candidates[0])
        print(similar_points_candidates[0].name, 'lost')
        tie = False
    else:
        min_value = min([player.suits for player in similar_points_candidates])
        similar_suits_candidates = [i for i in similar_points_candidates if i.suits == min_value]
        if len(similar_suits_candidates) == 1:
            players.remove(similar_suits_candidates[0])
            print(similar_suits_candidates[0].name, 'lost')
            tie = False
        else:
            min_value = min([player.ranks for player in similar_suits_candidates])
            similar_ranks_candidates = [i for i in similar_suits_candidates if i.ranks == min_value]
            if len(similar_ranks_candidates) == 1:
                players.remove(similar_ranks_candidates[0])
                print(similar_ranks_candidates[0].name, 'lost')
                tie = False
    if tie:
        print('It is tie.')

full_deck = []
current_deck = []
players = []

ranks = [(str(i), i) for i in range(2, 11)] + [('J', 11), ('Q', 12), ('K', 13), ('A', 20)]
suits = ('♠️', '❤️', '♦️', '♣️')
for suit in suits:
    for rank, points in ranks:
        full_deck.append({'suit': suit, 'rank': rank, 'points': points})
full_deck = full_deck * 4

for i in range(1, 4):
    players.append(Player(input(f'Please input Player {i} name: ')))

while len(players) > 1:
    print('Dealing cards')
    deal()
    for player in players: player.display()
    change = False
    for player in players:
        changeit = int(input(f'Which card from 1 to 5 would you like to replace for {player.name}? (Enter 0 for no change) - '))
        if 1 <= changeit <= 5:
            player.changecard(changeit)
            change = True
    if change:
        print("Players' cards after change:")
        for player in players: player.display()

    remove_loser()
print(f'And the winner is {players[0].name}.')