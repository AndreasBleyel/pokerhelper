import view as v
import model as m

class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.set_listener(self.change)

        self.was_selected = "Hand"

    def change(self, which_btn):
        if which_btn == "hand_board":
            if self.was_selected == "Hand":
                self.was_selected = "Board"
            else:
                self.was_selected = "Hand"
            self.view.set_btn_hand_board_text(self.was_selected)
        else:
            if self.was_selected == "Hand":
                self.model.hand += "H"
                self.view.set_player_hand(self.model.hand)
            else:
                self.model.board += "B"
                self.view.set_board(self.model.board)

            odds = self.model.calc_odds()
            self.view.set_odds_label(odds)

    def start(self):
        self.view.show()