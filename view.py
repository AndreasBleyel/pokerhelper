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

        self.player_hand = tk.Label(self.window, text="Ac,Bc").grid(row=2, column=0)

        self.img = Image.open("PNG/2C.png")
        self.img = self.img.resize(((55,75)), Image.ANTIALIAS)
        self.treff2 = ImageTk.PhotoImage(self.img)
        self.bt2 = tk.Button(self.window,command=lambda: self.change(),image=self.treff2).grid(row=0,column=0)


    def set_listener(self, listener):
        self.listener = listener

    def change(self):
        if self.listener:
            self.listener(self.player_hand)

    def set_odds_label(self, odds):
        self.odds.set(odds)

    def show(self):
        self.window.mainloop()