from PIL import Image
from PIL import ImageTk
from PIL import ImageFilter
import tkinter as tk

class View:
    def __init__(self, cards):

        self.listener = None
        self.cards = cards

        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.window.title("Texas Help'em")

        self.odds = tk.DoubleVar()
        self.odds_label = tk.Label(self.window, textvariable=self.odds).grid(row=1, column=0)

        self.player_hand_string = tk.StringVar()
        self.player_hand_label = tk.Label(self.window, text="Your Hand").grid(row=3, column=0)
        self.player_hand = tk.Label(self.window, textvariable=self.player_hand_string).grid(row=3, column=1)

        self.img = Image.open(self.cards[-1].img_path)
        self.img = self.img.resize(((55,75)), Image.ANTIALIAS)
        #self.img = self.img.filter(ImageFilter.DETAIL)
        self.card_back = ImageTk.PhotoImage(self.img)
        self.btn_hand_card1 = tk.Button(self.window, image=self.card_back, command= lambda: self.change("hand_card1")).grid(row=3, column=2)
        self.btn_hand_card2 = tk.Button(self.window, image=self.card_back, command= lambda: self.change("hand_card2")).grid(row=3, column=3)

        self.board_string = tk.StringVar()
        self.board_label = tk.Label(self.window, text="The Board").grid(row=2, column=0)
        self.board = tk.Label(self.window, textvariable=self.board_string).grid(row=2, column=1)
        self.btn_board_card1 = tk.Button(self.window, image=self.card_back).grid(row=2, column=2)
        self.btn_board_card2 = tk.Button(self.window, image=self.card_back).grid(row=2, column=3)
        self.btn_board_card3 = tk.Button(self.window, image=self.card_back).grid(row=2, column=4)
        self.btn_board_card4 = tk.Button(self.window, image=self.card_back).grid(row=2, column=5)
        self.btn_board_card5 = tk.Button(self.window, image=self.card_back).grid(row=2, column=6)

        self.hand_or_board_string = tk.StringVar()
        self.hand_or_board_string.set("Hand")
        self.btn_hand_or_board = tk.Button(self.window, command= lambda: self.change("hand_board"), textvariable=self.hand_or_board_string).grid(row=0, column=0)

        self.img = Image.open(self.cards[12].img_path)
        self.img = self.img.resize(((55,75)), Image.ANTIALIAS)
        self.treff2 = ImageTk.PhotoImage(self.img)
        self.btn_bt2 = tk.Button(self.window,command=lambda: self.change("card"),image=self.treff2).grid(row=4,column=0)

        self.img = Image.open(self.cards[1].img_path)
        self.img = self.img.resize(((55, 75)), Image.ANTIALIAS)
        self.treff3 = ImageTk.PhotoImage(self.img)
        self.btn_bt3 = tk.Button(self.window, command=lambda: self.change("card"), image=self.treff3).grid(row=4, column=1)

    def set_listener(self, listener):
        self.listener = listener

    def change(self, which_btn):
        if self.listener:
            self.listener(which_btn)

    def set_odds_label(self, odds):
        self.odds.set(odds)

    def set_player_hand(self, player_hand):
        self.player_hand_string.set(player_hand)

    def set_board(self, board):
        self.board_string.set(board)

    def set_btn_hand_board_text(self, value):
        self.hand_or_board_string.set(value)

    def show(self):
        self.window.mainloop()