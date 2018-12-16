from PIL import Image
from PIL import ImageTk
from PIL import ImageFilter
import tkinter as tk

class View:
    def __init__(self, cards):

        self.listener = None
        self.cards = cards
        self.card_images = []
        self.card_back = None

        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.window.title("Texas Help'em")

        self.btn_hand_card1 = None
        self.btn_hand_card2 = None
        self.btn_board_card1 = None
        self.btn_board_card2 = None
        self.btn_board_card3 = None
        self.btn_board_card4 = None
        self.btn_board_card5 = None
        self.show_cards()

        self.odds = tk.DoubleVar()
        self.odds_label = tk.Label(self.window, textvariable=self.odds).grid(row=0, column=8, columnspan = 4,padx=5, pady=5)

        self.board_label = tk.Label(self.window, text="Board").grid(row=2, column=1,padx=5, pady=5)
        self.board_hand = tk.Label(self.window, text="Hand").grid(row=3, column=1,padx=5, pady=5)

        self.btn_calc = tk.Button(self.window, command= lambda: self.change("calc"),
                                           text="Calc").grid(row=1, column=8, columnspan = 4)



    def set_listener(self, listener):
        self.listener = listener

    def change(self, which_btn):
        print("view: "+str(which_btn))
        if self.listener:
            self.listener(which_btn)

    def show_cards(self):
        img = Image.open(self.cards[-1].img_path)
        img = img.resize(((55, 75)), Image.ANTIALIAS)
        self.card_back = ImageTk.PhotoImage(img)
        self.btn_hand_card1 = tk.Button(self.window, image=self.card_back,
                                        command=lambda: self.change("hand_card1"))
        self.btn_hand_card1.grid(row=3, column=2)

        self.btn_hand_card2 = tk.Button(self.window, image=self.card_back,
                                        command=lambda: self.change("hand_card2"))
        self.btn_hand_card2.grid(row=3, column=3, pady = 10)

        self.btn_board_card1 = tk.Button(self.window, image=self.card_back,
                                         command=lambda: self.change("board_card1"))
        self.btn_board_card1.grid(row=2, column=2, pady=10)

        self.btn_board_card2 = tk.Button(self.window, image=self.card_back,
                                         command=lambda: self.change("board_card2"))
        self.btn_board_card2.grid(row=2, column=3)

        self.btn_board_card3 = tk.Button(self.window, image=self.card_back,
                                         command=lambda: self.change("board_card3"))
        self.btn_board_card3.grid(row=2, column=4)

        self.btn_board_card4 = tk.Button(self.window, image=self.card_back,
                                         command=lambda: self.change("board_card4"))
        self.btn_board_card4.grid(row=2, column=5)

        self.btn_board_card5 = tk.Button(self.window, image=self.card_back,
                                         command=lambda: self.change("board_card5"))
        self.btn_board_card5.grid(row=2, column=6)

        for i in range(len(self.cards)):
            self.img = Image.open(self.cards[i].img_path)
            self.img = self.img.resize(((55, 75)), Image.ANTIALIAS)
            self.card_images.append(ImageTk.PhotoImage(self.img))

        card_row = 4
        card_col = 0
        for i in range(52):
            if card_col == 13:
                card_col = 0
                card_row = card_row + 1
            self.btn = tk.Button(self.window,text="A", command= lambda i=i: self.change(i),
                                 image=self.card_images[i]).grid(row=card_row,column=card_col,padx=2, pady=1)
            card_col = card_col +1

    def set_odds_label(self, odds):
        self.odds.set(odds)

    def set_player_hand(self, player_hand):
        pass

    def set_board(self, board):
        pass

    def remove_all_highlights(self):
        self.btn_hand_card1.configure(bg="white")
        self.btn_hand_card2.configure(bg="white")
        self.btn_board_card1.configure(bg="white")
        self.btn_board_card2.configure(bg="white")
        self.btn_board_card3.configure(bg="white")
        self.btn_board_card4.configure(bg="white")
        self.btn_board_card5.configure(bg="white")

    def highlight_hand_card1(self):
        self.remove_all_highlights()
        self.btn_hand_card1.configure(bg="red")

    def set_image_hand_card1(self, index_image):
        self.btn_hand_card1.configure(image=self.card_images[index_image])

    def highlight_hand_card2(self):
        self.remove_all_highlights()
        self.btn_hand_card2.configure(bg="red")

    def set_image_hand_card2(self, index_image):
        self.btn_hand_card2.configure(image=self.card_images[index_image])

    def highlight_board_card1(self):
        self.remove_all_highlights()
        self.btn_board_card1.configure(bg="red")

    def set_image_board_card1(self, index_image):
        self.btn_board_card1.configure(image=self.card_images[index_image])

    def highlight_board_card2(self):
        self.remove_all_highlights()
        self.btn_board_card2.configure(bg="red")

    def set_image_board_card2(self, index_image):
        self.btn_board_card2.configure(image=self.card_images[index_image])

    def highlight_board_card3(self):
        self.remove_all_highlights()
        self.btn_board_card3.configure(bg="red")

    def set_image_board_card3(self, index_image):
        self.btn_board_card3.configure(image=self.card_images[index_image])

    def highlight_board_card4(self):
        self.remove_all_highlights()
        self.btn_board_card4.configure(bg="red")

    def set_image_board_card4(self, index_image):
        self.btn_board_card4.configure(image=self.card_images[index_image])

    def highlight_board_card5(self):
        self.remove_all_highlights()
        self.btn_board_card5.configure(bg="red")

    def set_image_board_card5(self, index_image):
        self.btn_board_card5.configure(image=self.card_images[index_image])

    def show(self):
        self.window.mainloop()