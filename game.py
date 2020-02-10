from Deck_Card_Player import Card, Deck, Player
import tkinter
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from tkinter import messagebox

RESOLUTION = "500x600"


def GUI_init(window):
    window.title("BlackJack Simulator --- By Shun | Sinmentis@foxmail.com")
    width_limit = (window.winfo_screenwidth() - int(RESOLUTION[:RESOLUTION.find("x")])) / 2
    height_limit = (window.winfo_screenheight() - int(RESOLUTION[RESOLUTION.find("x")+1:])) / 2
    window.geometry("{0}+{1:.0f}+{2:.0f}".format(RESOLUTION, width_limit, height_limit))



def init_game():
    player = Player("Shun")
    deck = Deck()
    deck.shuffle()
    return player, deck


def main():
    window = Tk()
    player, deck = init_game()
    GUI_init(window)
    window.mainloop()


if __name__ == "__main__":
    main()