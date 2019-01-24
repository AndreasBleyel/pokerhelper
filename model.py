import requests

import ApiValues
from Card import Card


class Model:

    def __init__(self):
        self._player_hand = [None] * 2
        self._board = [None] * 5
        self._cards = []
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

    def call_api(self):
        if self.board[0] and self.board[1] and self.board[2] and not self.board[3] and not self.board[4]:
            # flop
            hand = self.card_values.get(self.player_hand[0])+","+self.card_values.get(self.player_hand[1])
            board = self.card_values.get(self.board[0])+","+self.card_values.get(self.board[1])+","+self.card_values.get(self.board[2])
            request_url = ApiValues.api_url+"flop?board="+board+"&hole="+hand
            response = requests.get(request_url, headers = ApiValues.api_headers)
            if response.status_code != 200:
                print('API Call unsuccessful {}'.format(response.status_code))
                return 0
            else:
                json = response.json()

        elif self.board[0] and self.board[1] and self.board[2] and self.board[3] and not self.board[4]:
            # turn
            hand = self.card_values.get(self.player_hand[0]) + "," + self.card_values.get(self.player_hand[1])
            board = self.card_values.get(self.board[0]) + "," + self.card_values.get(
                self.board[1]) + "," + self.card_values.get(self.board[2])+ "," + self.card_values.get(self.board[3])
            request_url = ApiValues.api_url + "turn?board=" + board + "&hole=" + hand
            response = requests.get(request_url, headers=ApiValues.api_headers)
            if response.status_code != 200:
                print('API Call unsuccessful {}'.format(response.status_code))
                return 0
            else:
                json = response.json()
        elif self.board[0] and self.board[1] and self.board[2] and self.board[3] and self.board[4]:
            # river
            hand = self.card_values.get(self.player_hand[0]) + "," + self.card_values.get(self.player_hand[1])
            board = self.card_values.get(self.board[0]) + "," + self.card_values.get(
                self.board[1]) + "," + self.card_values.get(self.board[2]) + "," + self.card_values.get(self.board[3])+ "," + self.card_values.get(self.board[4])
            request_url = ApiValues.api_url + "river?board=" + board + "&hole=" + hand
            response = requests.get(request_url, headers=ApiValues.api_headers)
            if response.status_code != 200:
                print('API Call unsuccessful {}'.format(response.status_code))
                return 0
            else:
                json = response.json()
        else:
            #pre-flop
            hand = self.card_values.get(self.player_hand[0]) + "," + self.card_values.get(self.player_hand[1])
            request_url = ApiValues.api_url + "pre-flop?hole=" + hand
            response = requests.get(request_url, headers=ApiValues.api_headers)
            if response.status_code != 200:
                print('API Call unsuccessful {}'.format(response.status_code))
                return 0
            else:
                json = response.json()

        return json

    def calc_odds(self):
        if self.player_hand[0] and self.player_hand[1]:
            json = self.call_api()
            print(json)
        else:
            print("Player Hand missing")

        return json

    def create_cards(self):
        path = "PNG/"
        format = ".png"
        back = "blue_back"
        for i in range(52):
            card = Card(path+str(i)+format)
            self._cards.append(card)

        self._cards.append(Card(path+back+format))
        return self._cards



    # import requests
    #
    # def fetch_all():
    #     resp = requests.get('http://data.fixer.io/api/latest?access_key=be677e4869463accc8bdb0d690ba3e89&format=1')
    #     if resp.status_code != 200:
    #         print('API Call unsuccessful {}'.format(resp.status_code))
    #         return 1
    #     else:
    #         json = resp.json()
    #         return json
    #
    # def get_rate(json, symbol):
    #     return json["rates"][symbol]
    #
    # all_data = fetch_all()
    #
    # print("=============== Available rates ================")
    # for key in all_data["rates"]:
    #     print(key + " ", end="")
    # print("\n ============================================= ")
    #
    # symbol = input("Enter currency: ").upper()
    # value = float(input("Enter value: "))
    # custom_cur = Currency(value, symbol, get_rate(all_data, symbol))
    #
    # print("Your currency: {} - converted to EUR: {:.2f}".format(custom_cur, custom_cur.value / custom_cur.rate))
    # print("============================================= ")
    # usd1 = Currency(15, "USD", get_rate(all_data, "USD"))
    # eur1 = Currency(15)
    # print(usd1 + 5 + eur1)

