import ApiValues
import Errors

class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.set_listener(self.change)

        self.was_selected = "Hand"
        self.card_to_set = "hand_card1"
        self.odds = {
            "one_option": {
                "best": 0,
                "avg": 0,
                "rec_best": "",
                "rec_avg": ""
            },
            "two_options": {
                "best": 0,
                "avg": 0,
                "rec_best": "",
                "rec_avg": ""
            }
        }
        self.response = {}

    def change(self, which_btn):
        if which_btn == "calc":
            if self.model.evaluate_state_of_game() == "pre-flop":
                self.response = self.model.calculate_odds()
                if self.response["status"] is 200:
                    self.display_infos()
                else:
                    self.view.set_odd_infos_label(Errors.API_ERR+"\n{0[status]} {0[msg]}".format(self.response))
            elif self.model.evaluate_state_of_game() == "flop" or self.model.evaluate_state_of_game() == "turn" or self.model.evaluate_state_of_game() == "river":
                if self.is_bid_opp_set() and self.is_pot_size_set():
                    self.response = self.model.calculate_odds()
                    if self.response["status"] is 200:
                        self.display_infos()
                    else:
                        self.view.set_odd_infos_label(Errors.API_ERR + "\n{0[msg]}".format(self.response))
            elif self.model.evaluate_state_of_game() == "nohand":
                self.view.set_odd_infos_label(Errors.NO_HAND)
            elif self.model.evaluate_state_of_game() == "invalidboard":
                self.view.set_odd_infos_label(Errors.INV_BOARD)

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
        if self.get_state_of_game() == "pre-flop":
            infos = self.create_pre_flop_infos()
        elif self.get_state_of_game() == "flop":
            self.calc_odds()
            infos = self.create_flop_infos()
        elif self.get_state_of_game() == "turn":
            self.calc_odds()
            infos = self.create_turn_infos()
        elif self.get_state_of_game() == "river":
            infos = "river"

        self.view.set_odd_infos_label(infos)

    def create_pre_flop_infos(self):
        return self.create_hit_specific_hand_infos()

    def create_flop_infos(self):
        return self.create_hit_specific_hand_infos() + self.create_two_poss_infos() + self.create_one_poss_infos()

    def create_turn_infos(self):
        return self.create_hit_specific_hand_infos() + self.create_one_poss_infos()

    def create_hit_specific_hand_infos(self):
        if (self.get_state_of_game() == "pre-flop"):
            infos = "Chances to hit specific hand:\n" \
                    "High Card: {0[data][hit][HC]:.2%}\n" \
                    "1 Pair: {0[data][hit][1P]:.2%}\n" \
                    "2 Pairs: {0[data][hit][2P]:.2%}\n" \
                    "3 of a kind: {0[data][hit][3K]:.2%}\n" \
                    "Straight: {0[data][hit][ST]:.2%}\n" \
                    "Full House: {0[data][hit][FH]:.2%}\n" \
                    "Flush: {0[data][hit][FL]:.2%}\n" \
                    "4 of a kind: {0[data][hit][4K]:.2%}\n" \
                    "Straight Flush: {0[data][hit][SF]:.2%}\n\n" \
                    "Highest possible hand:\n" \
                    "{0[data][ranking][best][hand_name]} Rank: {0[data][ranking][best][rank]}\n" \
                    "Average possible hand:\n" \
                    "{0[data][ranking][average][hand_name]} Rank: {0[data][ranking][average][rank]}\n" \
                    "Worst possible hand:\n" \
                    "{0[data][ranking][worst][hand_name]} Rank: {0[data][ranking][worst][rank]}\n\n" \
                .format(self.response)
        else:
            infos = "Chances to hit specific hand:\n" \
                    "High Card: {0[data][me][hit][HC]:.2%}\n" \
                    "1 Pair: {0[data][me][hit][1P]:.2%}\n" \
                    "2 Pairs: {0[data][me][hit][2P]:.2%}\n" \
                    "3 of a kind: {0[data][me][hit][3K]:.2%}\n" \
                    "Straight: {0[data][me][hit][ST]:.2%}\n" \
                    "Full House: {0[data][me][hit][FH]:.2%}\n" \
                    "Flush: {0[data][me][hit][FL]:.2%}\n" \
                    "4 of a kind: {0[data][me][hit][4K]:.2%}\n" \
                    "Straight Flush: {0[data][me][hit][SF]:.2%}\n\n" \
                    "Highest possible hand:\n" \
                    "{0[data][me][ranking][best][hand_name]} Rank: {0[data][me][ranking][best][rank]}\n" \
                    "Average possible hand:\n" \
                    "{0[data][me][ranking][average][hand_name]} Rank: {0[data][me][ranking][average][rank]}\n" \
                    "Worst possible hand:\n" \
                    "{0[data][me][ranking][worst][hand_name]} Rank: {0[data][me][ranking][worst][rank]}\n\n" \
                .format(self.response)

        return infos

    def create_one_poss_infos(self):
        infos = "Odds one card to follow - best hand:\n" \
                "{0[one_option][best]:.2%} -> {0[one_option][rec_best]}\n" \
                "Odds one card to follow - avg hand:\n" \
                "{0[one_option][avg]:.2%} -> {0[one_option][rec_avg]}\n\n".format(self.odds)

        return infos

    def create_two_poss_infos(self):
        infos = "Odds Turn & River - best hand:\n" \
                "{0[two_options][best]:.2%} -> {0[two_options][rec_best]}\n" \
                "Odds Turn & River - avg hand:\n" \
                "{0[two_options][avg]:.2%} -> {0[two_options][rec_avg]}\n\n" \
            .format(self.odds)

        return infos

    def calc_odds(self):
        try:
            bid_opponent = float(self.view.get_bid_opponent())
            total_pot = float(self.view.get_total_pot())
            pot_odds = bid_opponent / (total_pot + bid_opponent * 2)
            self.odds["one_option"]["best"] = self.get_odds_best_hand()
            self.odds["one_option"]["avg"] = self.get_odds_avg_hand()
            self.odds["one_option"]["rec_best"] = "Call" if self.get_odds_best_hand() >= pot_odds else "Fold"
            self.odds["one_option"]["rec_avg"] = "Call" if self.get_odds_avg_hand() >= pot_odds else "Fold"

            self.odds["two_options"]["best"] = (self.get_odds_best_hand() - 0.01) * 2
            self.odds["two_options"]["avg"] = (self.get_odds_avg_hand() - 0.01) * 2
            self.odds["two_options"]["rec_best"] = "Call" if self.odds["two_options"]["best"] >= pot_odds else "Fold"
            self.odds["two_options"]["rec_avg"] = "Call" if self.odds["two_options"]["avg"] >= pot_odds else "Fold"
        except ZeroDivisionError:
            self.view.set_odd_infos_label(Errors.NO_POT)

    def is_pot_size_set(self):
        try:
            if float(self.view.get_total_pot()) > 0:
                return True
            else:
                self.view.set_odd_infos_label(Errors.NEG_NR+" Pot Size")
                return False
        except (ValueError, UnboundLocalError) as e:
            self.view.set_odd_infos_label(Errors.NO_POT+"\n"+str(e))
            return False

    def is_bid_opp_set(self):
        try:
            if float(self.view.get_bid_opponent()) >= 0:
                return True
            else:
                self.view.set_odd_infos_label(Errors.NEG_NR+" for Bid Opponent")
                return False
        except ValueError:
            self.view.set_odd_infos_label(Errors.NOT_A_NR+" Bid Opponent")
            return False
        except UnboundLocalError:
            self.view.set_bid_opponent_zero()
            return True

    def get_code_best_possible_hand(self):
        return self.response.get("data").get("me").get("ranking").get("best").get("hand_code")

    def get_code_avg_possible_hand(self):
        return self.response.get("data").get("me").get("ranking").get("average").get("hand_code")

    def get_odds_best_hand(self):
        return self.response.get("data").get("me").get("hit").get(self.get_code_best_possible_hand())

    def get_odds_avg_hand(self):
        return self.response.get("data").get("me").get("hit").get(self.get_code_avg_possible_hand())

    def get_state_of_game(self):
        if self.response.get("state") == "pre-flop":
            return "pre-flop"
        elif self.response.get("state") == "flop":
            return "flop"
        elif self.response.get("state") == "turn":
            return "turn"
        elif self.response.get("state") == "river":
            return "river"

    def start(self):
        self.view.highlight_hand_card1()
        self.view.show()
