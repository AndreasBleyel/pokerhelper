import view as v
import model as m

class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.set_listener(self.calc_odds)

    def calc_odds(self, hand):
        odds = self.model.calc_odds(hand)
        self.view.set_odds_label(odds)


    def start(self):
        self.view.show()