import random


class Deck:
    points = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
              "J": 11, "Q": 12, "K": 13, "A": 20}

    def __init__(self):
        suits = ('♠️', '❤️', '♦️', '♣️')
        values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
        self.cards = [{'suit': suit, 'value': value} for suit in suits for value in values] * 4

    def shuffle(self):
        random.shuffle(self.cards)

    def get_random_card(self):
        if not self.cards:
            raise ValueError("The deck is empty!")
        return self.cards.pop()

    def get_card_points(self, card):
        return self.points.get(card['value'], 0)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_cards(self, deck, count=5):
        self.hand = []  # Clear the hand before drawing new cards
        for _ in range(count):
            self.hand.append(deck.get_random_card())

    def calculate_score(self, deck):
        return sum(deck.get_card_points(card) for card in self.hand)

    def most_common_suit_count(self):
        suits = [card['suit'] for card in self.hand]
        return max(suits.count(suit) for suit in set(suits))

    def most_common_value_count(self):
        values = [card['value'] for card in self.hand]
        return max(values.count(value) for value in set(values))

    def change_card(self, deck):
        print(f"\n{self.name}, your current hand:")
        for i, card in enumerate(self.hand, 1):
            print(f"[{i}] {card['value']}{card['suit']}")

        change = input("Do you want to change a card? (yes/no): ").strip().lower()
        if change == "yes":
            try:
                index = int(input("Enter the index (1-5) of the card you want to change: ")) - 1
                if 0 <= index < len(self.hand):
                    self.hand[index] = deck.get_random_card()
                    print(f"Card changed! New card: {self.hand[index]['value']}{self.hand[index]['suit']}")
                else:
                    print("Invalid index!")
            except (ValueError, IndexError):
                print("Invalid input! No card changed.")

    def display_hand(self):
        return " ".join(f"{card['value']}{card['suit']}" for card in self.hand)


def determine_loser(players, deck):
    scores = [player.calculate_score(deck) for player in players]
    min_score = min(scores)
    bottom_players = [player for player, score in zip(players, scores) if score == min_score]

    if len(bottom_players) == 1:
        return bottom_players[0]

    min_suit_count = min(player.most_common_suit_count() for player in bottom_players)
    bottom_players = [player for player in bottom_players if player.most_common_suit_count() == min_suit_count]

    if len(bottom_players) == 1:
        return bottom_players[0]

    min_value_count = min(player.most_common_value_count() for player in bottom_players)
    bottom_players = [player for player in bottom_players if player.most_common_value_count() == min_value_count]

    if len(bottom_players) == 1:
        return bottom_players[0]


def play_game():
    print("\nWelcome to the Card Game!\n")
    print("Each player will draw cards, and the player with the highest score wins!")
    print("If there is a tie, additional rules will determine the loser.\n")

    deck = Deck()
    deck.shuffle()

    players = []
    for i in range(3):
        name = input(f"Enter name for Player {i + 1}: ").strip()
        players.append(Player(name))

    while len(players) > 1:
        print("\nDealing cards...\n")
        for player in players:
            player.draw_cards(deck)

        print("Player Hands and Scores:")
        for player in players:
            print(f"{player.name}: {player.display_hand()} | Score: {player.calculate_score(deck)}")

        print("\nTime for card changes!")
        for player in players:
            player.change_card(deck)

        print("\nUpdated Hands:")
        for player in players:
            print(f"{player.name}: {player.display_hand()} | Score: {player.calculate_score(deck)}")

        loser = determine_loser(players, deck)
        print(f"\n{loser.name} is eliminated!")

        if loser:
            players.remove(loser)
        else:
            print("It is tie.")

        if len(deck.cards) < len(players) * 5 + 3:
            print("\nReshuffling the deck...")
            deck = Deck()
            deck.shuffle()

    print(f"\nCongratulations, {players[0].name}! You are the winner!\n")


if __name__ == "__main__":
    play_game()
