import random
import requests
import ApiValues

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

    def call_api(self):
        if self.board[0] and self.board[1] and self.board[2] and not self.board[3] and not self.board[4]:
            # flop
            print(self.board[0])
            #response = requests.get(ApiValues.api_url+"flop?board=As%2C2h%2CTh&hole=Ac%2C3c", headers = ApiValues.api_headers)
            #json = response.json()
            #print(json)

        elif self.board[0] and self.board[1] and self.board[2] and self.board[3] and not self.board[4]:
            # turn
            print("turn")

        elif self.board[0] and self.board[1] and self.board[2] and self.board[3] and self.board[4]:
            # river
            print("river")

        return 0

    def calc_odds(self):
        if self.player_hand[0] and self.player_hand[1]:
            self.call_api()
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

