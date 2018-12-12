from PIL import Image
from PIL import ImageTk
import tkinter as tk

class View:
    def __init__(self):

        self.listener = None

        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.window.title("Texas Help'em")

        self.odds = tk.DoubleVar()
        self.odds_label = tk.Label(self.window, textvariable=self.odds).grid(row=1, column=0)

        self.player_hand_label = tk.Label(self.window, text="Your Hand").grid(row=2, column=0)
        self.player_hand = tk.Label(self.window, text="Ac,Bc").grid(row=2, column=1)

        self.board_label = tk.Label(self.window, text="The Board").grid(row=3, column=0)
        self.board = tk.Label(self.window, text="Ah,Bh,10s,4s,2s").grid(row=3, column=1)

        self.hand_or_board_string = tk.StringVar()
        self.hand_or_board_string.set("Hand")
        self.btn_hand_or_board = tk.Button(self.window, command= lambda: self.change("hand_board"), textvariable=self.hand_or_board_string).grid(row=0, column=0)

        self.img = Image.open("PNG/2C.png")
        self.img = self.img.resize(((55,75)), Image.ANTIALIAS)
        self.treff2 = ImageTk.PhotoImage(self.img)
        self.btn_bt2 = tk.Button(self.window,command=lambda: self.change("card"),image=self.treff2).grid(row=4,column=0)

        self.img = Image.open("PNG/3C.png")
        self.img = self.img.resize(((55, 75)), Image.ANTIALIAS)
        self.treff3 = ImageTk.PhotoImage(self.img)
        self.btn_bt3 = tk.Button(self.window, command=lambda: self.change("card"), image=self.treff3).grid(row=4, column=1)

    def set_listener(self, listener):
        self.listener = listener

    def change(self, which_btn):
        if self.listener:
            self.listener(self.player_hand, self.board, which_btn)

    def set_odds_label(self, odds):
        self.odds.set(odds)

    def set_btn_hand_board_text(self, value):
        self.hand_or_board_string.set(value)

    def show(self):
        self.window.mainloop()