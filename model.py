import random

class Model:

    def __init__(self):
        self._hand = ""
        self._board = ""

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):
        self._hand = value

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value):
        self._board = value

    def calc_odds(self):
        return random.randint(1,10)
