import view as v
import model as m
import Card


class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.set_listener(self.change)

        self.was_selected = "Hand"
        self.card_to_set = "hand_card1"

        self.player_hand = []

    def change(self, which_btn):
        if which_btn == "calc":
            print(self.model.calc_odds())
        elif which_btn == "hand_card1" or which_btn == "hand_card2" or which_btn == "board_card1" \
                or which_btn == "board_card2" or which_btn == "board_card3" or which_btn == "board_card4" \
                or which_btn == "board_card5":
            self.highlight_selected_place(which_btn)
            self.card_to_set = which_btn
        else:
            if self.card_to_set == "hand_card1":
                self.view.set_image_hand_card1(which_btn)
                self.card_to_set = "hand_card2"
                self.highlight_selected_place(self.card_to_set)
            elif self.card_to_set == "hand_card2":
                self.view.set_image_hand_card2(which_btn)
                self.card_to_set = "board_card1"
                self.highlight_selected_place(self.card_to_set)
            elif self.card_to_set == "board_card1":
                self.view.set_image_board_card1(which_btn)
                self.card_to_set = "board_card2"
                self.highlight_selected_place(self.card_to_set)
            elif self.card_to_set == "board_card2":
                self.view.set_image_board_card2(which_btn)
                self.card_to_set = "board_card3"
                self.highlight_selected_place(self.card_to_set)
            elif self.card_to_set == "board_card3":
                self.view.set_image_board_card3(which_btn)
                self.card_to_set = "board_card4"
                self.highlight_selected_place(self.card_to_set)
            elif self.card_to_set == "board_card4":
                self.view.set_image_board_card4(which_btn)
                self.card_to_set = "board_card5"
                self.highlight_selected_place(self.card_to_set)
            elif self.card_to_set == "board_card5":
                self.view.set_image_board_card5(which_btn)
                self.card_to_set = "hand_card1"
                self.highlight_selected_place(self.card_to_set)

        odds = self.model.calc_odds()
        self.view.set_odds_label(which_btn)

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
