import random

from Card import Card


class Model:

    def __init__(self):
        self._hand = ""
        self._board = ""
        self._cards = []

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

    def create_cards(self):
        path = "PNG/"
        format = ".png"
        back = "blue_back"
        for i in range(13):
            card = Card(path+str(i)+format)
            self._cards.append(card)

        self._cards.append(Card(path+back+format))
        return self._cards