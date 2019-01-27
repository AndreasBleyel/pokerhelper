import requests
import view
import ApiValues
from Card import Card


class Model:

    def __init__(self):
        self._player_hand = [None] * 2
        self._board = [None] * 5
        self._cards = []
        self.json = {}

        self.card_values = {
            0: "2c",
            1: "3c",
            2: "4c",
            3: "5c",
            4: "6c",
            5: "7c",
            6: "8c",
            7: "9c",
            8: "Tc",
            9: "Jc",
            10: "Qc",
            11: "Kc",
            12: "Ac",

            13: "2d",
            14: "3d",
            15: "4d",
            16: "5d",
            17: "6d",
            18: "7d",
            19: "8d",
            20: "9d",
            21: "Td",
            22: "Jd",
            23: "Qd",
            24: "Kd",
            25: "Ad",

            26: "2h",
            27: "3h",
            28: "4h",
            29: "5h",
            30: "6h",
            31: "7h",
            32: "8h",
            33: "9h",
            34: "Th",
            35: "Jh",
            36: "Qh",
            37: "Kh",
            38: "Ah",

            39: "2s",
            40: "3s",
            41: "4s",
            42: "5s",
            43: "6s",
            44: "7s",
            45: "8s",
            46: "9s",
            47: "Ts",
            48: "Js",
            49: "Qs",
            50: "Ks",
            51: "As"
        }

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

    def calculate_odds(self):
        if self.evaluate_state_of_game() == "flop":
            # flop
            hand = self.card_values.get(self.player_hand[0]) + "," + self.card_values.get(self.player_hand[1])
            board = self.card_values.get(self.board[0]) + "," + self.card_values.get(
                self.board[1]) + "," + self.card_values.get(self.board[2])
            request_url = ApiValues.api_url + "flop?board=" + board + "&hole=" + hand
            self.make_call(request_url, "flop")

        elif self.evaluate_state_of_game() == "turn":
            # turn
            hand = self.card_values.get(self.player_hand[0]) + "," + self.card_values.get(self.player_hand[1])
            board = self.card_values.get(self.board[0]) + "," + self.card_values.get(
                self.board[1]) + "," + self.card_values.get(self.board[2]) + "," + self.card_values.get(self.board[3])
            request_url = ApiValues.api_url + "turn?board=" + board + "&hole=" + hand
            self.make_call(request_url, "turn")

        elif self.evaluate_state_of_game() == "river":
            # river
            hand = self.card_values.get(self.player_hand[0]) + "," + self.card_values.get(self.player_hand[1])
            board = self.card_values.get(self.board[0]) + "," + self.card_values.get(
                self.board[1]) + "," + self.card_values.get(self.board[2]) + "," + self.card_values.get(
                self.board[3]) + "," + self.card_values.get(self.board[4])
            request_url = ApiValues.api_url + "river?board=" + board + "&hole=" + hand
            self.make_call(request_url, "river")

        elif self.evaluate_state_of_game() == "pre-flop":
            # pre-flop.json
            hand = self.card_values.get(self.player_hand[0]) + "," + self.card_values.get(self.player_hand[1])
            request_url = ApiValues.api_url + "pre-flop?hole=" + hand
            self.make_call(request_url, "pre-flop")
        else:
            self.json = {"state": "nohand"}

        return self.json

    def make_call(self, request_url, state):
        try:
            response = requests.get(request_url, headers=ApiValues.api_headers)
            if response.status_code != 200:
                self.json["status"] = response.status_code
                self.json["msg"] = response.json()["message"]
            else:
                self.json = response.json()
                self.json["state"] = state
        except requests.exceptions.RequestException as e:
            self.json["status"] = 0
            self.json["msg"] = e

    def evaluate_state_of_game(self):
        if self.player_hand[0] is not None and self.player_hand[1] is not None:
            if self.board[0] is not None and self.board[1] is not None and self.board[2] is not None and self.board[
                3] is None and self.board[4] is None:
                return "flop"
            elif self.board[0] is not None and self.board[1] is not None and self.board[2] is not None and self.board[
                3] is not None and self.board[4] is None:
                return "turn"
            elif self.board[0] is not None and self.board[1] is not None and self.board[2] is not None and self.board[
                3] is not None and self.board[4] is not None:
                return "river"
            elif self.board[0] is None and self.board[1] is None and self.board[2] is None and \
                    self.board[3] is None and self.board[4] is None:
                return "pre-flop"
            else:
                return "invalidboard"
        else:
            return "nohand"

    def create_cards(self):
        path = "PNG/"
        format = ".png"
        back = "blue_back"
        for i in range(52):
            card = Card(path + str(i) + format)
            self._cards.append(card)

        self._cards.append(Card(path + back + format))
        return self._cards
