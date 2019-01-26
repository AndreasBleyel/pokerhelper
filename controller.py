import ApiValues


class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.set_listener(self.change)

        self.was_selected = "Hand"
        self.card_to_set = "hand_card1"

        # dict to save api response
        self.response = {}

    def change(self, which_btn):
        if which_btn == "calc":
            try:
                self.response = ApiValues.api_response
                self.display_infos()
            except UnboundLocalError:
                print("Hand missing")
        elif which_btn == "hand_card1" or which_btn == "hand_card2" or which_btn == "board_card1" \
                or which_btn == "board_card2" or which_btn == "board_card3" or which_btn == "board_card4" \
                or which_btn == "board_card5":
            self.highlight_selected_place(which_btn)
            self.card_to_set = which_btn
        elif which_btn == "del":
            if self.card_to_set == "hand_card1":
                self.model.player_hand[0] = None
                self.view.set_image_hand_card1(which_btn)
            elif self.card_to_set == "hand_card2":
                self.model.player_hand[1] = None
                self.view.set_image_hand_card2(which_btn)
            elif self.card_to_set == "board_card1":
                self.model.board[0] = None
                self.view.set_image_board_card1(which_btn)
            elif self.card_to_set == "board_card2":
                self.model.board[1] = None
                self.view.set_image_board_card2(which_btn)
            elif self.card_to_set == "board_card3":
                self.model.board[2] = None
                self.view.set_image_board_card3(which_btn)
            elif self.card_to_set == "board_card4":
                self.model.board[3] = None
                self.view.set_image_board_card4(which_btn)
            elif self.card_to_set == "board_card5":
                self.model.board[4] = None
                self.view.set_image_board_card5(which_btn)
        else:
            if self.card_to_set == "hand_card1" and (
                    which_btn not in self.model.player_hand and which_btn not in self.model.board):
                self.model.player_hand[0] = which_btn
                self.view.set_image_hand_card1(which_btn)
                self.card_to_set = "hand_card2"
                self.highlight_selected_place(self.card_to_set)
            elif self.card_to_set == "hand_card2" and (
                    which_btn not in self.model.player_hand and which_btn not in self.model.board):
                self.model.player_hand[1] = which_btn
                self.view.set_image_hand_card2(which_btn)
                self.card_to_set = "board_card1"
                self.highlight_selected_place(self.card_to_set)
            elif self.card_to_set == "board_card1" and (
                    which_btn not in self.model.player_hand and which_btn not in self.model.board):
                self.model.board[0] = which_btn
                self.view.set_image_board_card1(which_btn)
                self.card_to_set = "board_card2"
                self.highlight_selected_place(self.card_to_set)
            elif self.card_to_set == "board_card2" and (
                    which_btn not in self.model.player_hand and which_btn not in self.model.board):
                self.model.board[1] = which_btn
                self.view.set_image_board_card2(which_btn)
                self.card_to_set = "board_card3"
                self.highlight_selected_place(self.card_to_set)
            elif self.card_to_set == "board_card3" and (
                    which_btn not in self.model.player_hand and which_btn not in self.model.board):
                self.model.board[2] = which_btn
                self.view.set_image_board_card3(which_btn)
                self.card_to_set = "board_card4"
                self.highlight_selected_place(self.card_to_set)
            elif self.card_to_set == "board_card4" and (
                    which_btn not in self.model.player_hand and which_btn not in self.model.board):
                self.model.board[3] = which_btn
                self.view.set_image_board_card4(which_btn)
                self.card_to_set = "board_card5"
                self.highlight_selected_place(self.card_to_set)
            elif self.card_to_set == "board_card5" and (
                    which_btn not in self.model.player_hand and which_btn not in self.model.board):
                self.model.board[4] = which_btn
                self.view.set_image_board_card5(which_btn)
                self.card_to_set = "hand_card1"
                self.highlight_selected_place(self.card_to_set)

    def highlight_selected_place(self, place):
        if place == "hand_card1":
            self.view.highlight_hand_card1()
        elif place == "hand_card2":
            self.view.highlight_hand_card2()
        elif place == "board_card1":
            self.view.highlight_board_card1()
        elif place == "board_card2":
            self.view.highlight_board_card2()
        elif place == "board_card3":
            self.view.highlight_board_card3()
        elif place == "board_card4":
            self.view.highlight_board_card4()
        elif place == "board_card5":
            self.view.highlight_board_card5()

    def display_infos(self):
        if self.response.get("state") == "pre-flop":
            self.display_preflop_infos()
        elif self.response.get("state") == "flop":
            pass
        elif self.response.get("state") == "turn":
            pass
        elif self.response.get("state") == "river":
            pass

    def display_preflop_infos(self):
        print(self.response)
        infos = "Chances to hit specific hand:\n" \
                "1 Pair: " + str(self.response.get("data").get("hit").get("1P")) + "\n" + \
                "2 Pairs: " + str(self.response.get("data").get("hit").get("2P"))

        infos3 = "Chances to hit specific hand:\n" \
                 "High Card: {0[data][hit][HC]:.2%}\n" \
                 "1 Pair: {0[data][hit][1P]:.2%}\n" \
                 "2 Pairs: {0[data][hit][2P]:.2%}\n" \
                 "3 of a kind: {0[data][hit][3K]:.2%}\n" \
                 "Straight: {0[data][hit][ST]:.2%}\n" \
                 "Full House: {0[data][hit][FH]:.2%}\n" \
                 "Flush: {0[data][hit][FL]:.2%}\n" \
                 "4 of a kind: {0[data][hit][4K]:.2%}\n" \
                 "Straight Flush: {0[data][hit][SF]:.2%}" \
            .format(self.response)
        self.view.set_odd_infos_label(infos3)


    def start(self):
        self.view.highlight_hand_card1()
        self.view.show()
