import ApiValues
import json

class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.set_listener(self.change)

        self.was_selected = "Hand"
        self.card_to_set = "hand_card1"

    def change(self, which_btn):
        if which_btn == "calc":
            try:
                api_response = json.dumps(self.model.calc_odds(), indent=4, sort_keys=True)
                self.view.set_json_label(api_response)
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

    def start(self):
        self.view.highlight_hand_card1()
        self.view.show()
