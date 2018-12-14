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

    def change(self, which_btn):
        if which_btn == "hand_board":
            if self.was_selected == "Hand":
                self.was_selected = "Board"
            else:
                self.was_selected = "Hand"
            self.view.set_btn_hand_board_text(self.was_selected)
        elif which_btn == "hand_card1":
            pass

        odds = self.model.calc_odds()
        self.view.set_odds_label(which_btn)

    def start(self):
        self.view.show()

