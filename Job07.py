import random


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.score = 0

    def hit(self, card):
        self.cards.append(card)
        self.score += card.value

    def stand(self):
        pass

    def reset(self):
        self.cards = []
        self.score = 0


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 11):
            for j in ['spades', 'hearts', 'diamonds', 'clubs']:
                self.cards.append(Card(str(i), j, i))
        for j in ['spades', 'hearts', 'diamonds', 'clubs']:
            self.cards.append(Card('J', j, 10))
            self.cards.append(Card('Q', j, 10))
            self.cards.append(Card('K', j, 10))
            self.cards.append(Card('A', j, 11))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, player):
        card = self.cards.pop()
        player.hit(card)


class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player1 = Player(input("Enter player 1 name: "))
        self.player2 = Player(input("Enter player 2 name: "))
        self.game_over = False

    def get_input(self):
        choice = input(
            f"{self.current_player.name}, would you like to hit or stand? ")
        while choice not in ["hit", "stand"]:
            choice = input(
                f"{self.current_player.name}, please enter hit or stand: ")
        if choice == "hit":
            self.deck.deal(self.current_player)
            print(
                f"{self.current_player.name} drew {self.current_player.cards[-1]}")
            if self.current_player.score > 21:
                print(f"{self.current_player.name} busts!")
                self.game_over = True
        else:
            self.current_player.stand()

    def change_turn(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def play_game(self):
        while not self.game_over:
            self.current_player = self.player1
            while True:
                self.get_input()
                if self.game_over or self.current_player.score == 21:
                    break
            self.change_turn()

        if self.player1.score > 21:
            print(f"{self.player1.name} busts, {self.player2.name} wins!")
        elif self.player2.score > 21:
            print(f"{self.player2.name} busts, {self.player1.name} wins!")
        elif self.player1.score == self.player2.score:
            print("It's a tie!")
        elif self.player1.score > self.player2.score:
            print(f"{self.player1.name} wins with {self.player1.score}!")
        else:
            print(f"{self.player2.name} wins with {self.player2.score}!")


game = Game()
game.play_game()
