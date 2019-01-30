import tkinter as tk

from PIL import Image
from PIL import ImageTk


class View:
    def __init__(self, cards):

        self.listener = None
        self.cards = cards
        self.card_images = []
        self.card_back = None

        self.window = tk.Tk()
        self.window.title("Texas Help'em")
        self.window.minsize(1200, 535)

        self.board_bg_frame = tk.Frame(master=self.window, bg="#076324")
        self.board_bg_frame.place(x=5, y=5, width=365, height=190)

        self.card_frame = tk.Frame(master=self.window, bg='#FFCFC9')
        self.card_frame.place(x=5, y=200, width=790, height=330)

        self.button_frame = tk.Frame(master=self.window, bg="#FFABAB")
        self.button_frame.place(x=400, y=90, width=280, height=105)

        self.pot_infos_frame = tk.Frame(master=self.window, bg="#FFCDCD")
        self.pot_infos_frame.place(x=400, y=5, width=280, height=90)

        self.display_infos_frame = tk.Frame(master=self.window, bg="#FFFCFC")
        self.display_infos_frame.place(x=800, y=5, width=380, height=525)

        self.btn_hand_card1 = None
        self.btn_hand_card2 = None
        self.btn_board_card1 = None
        self.btn_board_card2 = None
        self.btn_board_card3 = None
        self.btn_board_card4 = None
        self.btn_board_card5 = None
        self.show_cards()

        self.odd_infos = tk.StringVar()
        self.odd_infos_label = tk.Label(master=self.display_infos_frame, anchor=tk.NW, justify=tk.LEFT, textvariable=self.odd_infos)
        self.odd_infos_label.place(x=5, y=5, width=370, height=515)

        self.board_label = tk.Label(self.window, text="Board").grid(row=0, column=1, padx=5, pady=5)
        self.board_hand = tk.Label(self.window, text="Hand").grid(row=1, column=1, padx=5, pady=5)

        self.btn_calc = tk.Button(master=self.button_frame, command=lambda: self.change("calc"),
                                  text="Calc")
        self.btn_calc.place(x=5, y=10)

        self.btn_del_card = tk.Button(self.button_frame, command=lambda: self.change("del"),
                                      text="Remove Card")
        self.btn_del_card.place(x=5, y=45)

        self.btn_del_all = tk.Button(self.button_frame, command=lambda: self.change("del_all"),
                                      text="Remove All")
        self.btn_del_all.place(x=125, y=45)

        self.bid_opp_label = tk.Label(master=self.pot_infos_frame, text="Bid Opponent:")
        self.bid_opp_label.place(x=5, y=5)
        self.bid_opp = tk.Entry(master=self.pot_infos_frame)
        self.bid_opp.insert(0,0)
        self.bid_opp.place(x=100, y=5)

        self.total_pot_label = tk.Label(master=self.pot_infos_frame, text="Total Pot:")
        self.total_pot_label.place(x=5, y=55)
        self.total_pot = tk.Entry(master=self.pot_infos_frame)
        self.total_pot.insert(0,0)
        self.total_pot.place(x=100, y=55)


    def set_listener(self, listener):
        self.listener = listener

    def change(self, which_btn):
        print("view: " + str(which_btn))
        if self.listener:
            self.listener(which_btn)

    def show_cards(self):
        img = Image.open(self.cards[-1].img_path)
        img = img.resize(((55, 75)), Image.ANTIALIAS)
        self.card_back = ImageTk.PhotoImage(img)
        self.btn_hand_card1 = tk.Button(self.window, image=self.card_back,
                                        command=lambda: self.change("hand_card1"))
        self.btn_hand_card1.grid(row=1, column=2)

        self.btn_hand_card2 = tk.Button(self.window, image=self.card_back,
                                        command=lambda: self.change("hand_card2"))
        self.btn_hand_card2.grid(row=1, column=3, pady=10)

        self.btn_board_card1 = tk.Button(self.window, image=self.card_back,
                                         command=lambda: self.change("board_card1"))
        self.btn_board_card1.grid(row=0, column=2, pady=10)

        self.btn_board_card2 = tk.Button(self.window, image=self.card_back,
                                         command=lambda: self.change("board_card2"))
        self.btn_board_card2.grid(row=0, column=3)

        self.btn_board_card3 = tk.Button(self.window, image=self.card_back,
                                         command=lambda: self.change("board_card3"))
        self.btn_board_card3.grid(row=0, column=4)

        self.btn_board_card4 = tk.Button(self.window, image=self.card_back,
                                         command=lambda: self.change("board_card4"))
        self.btn_board_card4.grid(row=0, column=5)

        self.btn_board_card5 = tk.Button(self.window, image=self.card_back,
                                         command=lambda: self.change("board_card5"))
        self.btn_board_card5.grid(row=0, column=6)

        for i in range(len(self.cards)):
            img = Image.open(self.cards[i].img_path)
            img = img.resize(((55, 75)), Image.ANTIALIAS)
            self.card_images.append(ImageTk.PhotoImage(img))

        reihe = 0
        spalte = 0
        xwert = 5
        ywert = 5
        for i in range(52):
            if spalte == 13:
                spalte = 0
                reihe = reihe + 1
                ywert = ywert + 80
                xwert = 5

            self.btn = tk.Button(master=self.card_frame, command=lambda i=i: self.change(i),
                                 image=self.card_images[i])
            self.btn.place(x=xwert, y=ywert)
            xwert = xwert + 60
            spalte = spalte + 1

    def set_odd_infos_label(self, infos):
        self.odd_infos.set(infos)

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
        if index_image == "del":
            self.btn_hand_card1.configure(image=self.card_images[-1])
        else:
            self.btn_hand_card1.configure(image=self.card_images[index_image])

    def highlight_hand_card2(self):
        self.remove_all_highlights()
        self.btn_hand_card2.configure(bg="red")

    def set_image_hand_card2(self, index_image):
        if index_image == "del":
            self.btn_hand_card2.configure(image=self.card_images[-1])
        else:
            self.btn_hand_card2.configure(image=self.card_images[index_image])

    def highlight_board_card1(self):
        self.remove_all_highlights()
        self.btn_board_card1.configure(bg="red")

    def set_image_board_card1(self, index_image):
        if index_image == "del":
            self.btn_board_card1.configure(image=self.card_images[-1])
        else:
            self.btn_board_card1.configure(image=self.card_images[index_image])

    def highlight_board_card2(self):
        self.remove_all_highlights()
        self.btn_board_card2.configure(bg="red")

    def set_image_board_card2(self, index_image):
        if index_image == "del":
            self.btn_board_card2.configure(image=self.card_images[-1])
        else:
            self.btn_board_card2.configure(image=self.card_images[index_image])

    def highlight_board_card3(self):
        self.remove_all_highlights()
        self.btn_board_card3.configure(bg="red")

    def set_image_board_card3(self, index_image):
        if index_image == "del":
            self.btn_board_card3.configure(image=self.card_images[-1])
        else:
            self.btn_board_card3.configure(image=self.card_images[index_image])

    def highlight_board_card4(self):
        self.remove_all_highlights()
        self.btn_board_card4.configure(bg="red")

    def set_image_board_card4(self, index_image):
        if index_image == "del":
            self.btn_board_card4.configure(image=self.card_images[-1])
        else:
            self.btn_board_card4.configure(image=self.card_images[index_image])

    def highlight_board_card5(self):
        self.remove_all_highlights()
        self.btn_board_card5.configure(bg="red")

    def set_image_board_card5(self, index_image):
        if index_image == "del":
            self.btn_board_card5.configure(image=self.card_images[-1])
        else:
            self.btn_board_card5.configure(image=self.card_images[index_image])

    # def get_bid_player(self):
    #     return self.bid_player.get()

    def get_bid_opponent(self):
        return self.bid_opp.get()

    def set_bid_opponent_zero(self):
        self.bid_opp.insert(0,0)

    def get_total_pot(self):
        return self.total_pot.get()

    def show(self):
        self.window.mainloop()
