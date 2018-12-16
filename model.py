import random

from Card import Card

class Model:

    def __init__(self):
        self._player_hand = [None] * 2
        self._board = [None] * 5
        self._cards = []

    @property
    def player_hand(self):
        return self._player_hand

    @player_hand.setter
    def player_hand(self, value):
        self.player_hand = value

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value):
        self._board = value

    def calc_odds(self):
        if self.player_hand[0] and self.player_hand[1]:
            if self.board[0] and self.board[1] and self.board[2] and not self.board[3] and not self.board[4]:
                #flop
                print("flop")
                pass
            elif self.board[0] and self.board[1] and self.board[2] and self.board[3] and not self.board[4]:
                #turn
                print("turn")
                pass
            elif self.board[0] and self.board[1] and self.board[2] and self.board[3] and self.board[4]:
                #river
                print("river")
                pass
        else:
            print("Player Hand missing")

        return random.randint(1,10)

    def create_cards(self):
        path = "PNG/"
        format = ".png"
        back = "blue_back"
        for i in range(52):
            card = Card(path+str(i)+format)
            self._cards.append(card)

        self._cards.append(Card(path+back+format))
        return self._cards