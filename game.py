from tkinter import *

from blackjack import Blackjack
from player import Player

RESOLUTION = "500x600"


def GUI_init():
    window = Tk()
    window.title("BlackJack Simulator")
    width_limit = (window.winfo_screenwidth() - int(RESOLUTION[:RESOLUTION.find("x")])) / 2
    height_limit = (window.winfo_screenheight() - int(RESOLUTION[RESOLUTION.find("x") + 1:])) / 2
    window.geometry("{0}+{1:.0f}+{2:.0f}".format(RESOLUTION, width_limit, height_limit))

    window = draw_GUI(window)

    return window


def draw_GUI(windows):

    return windows


def main():
    banker = Player("Banker")
    player = Player("Player")
    game = Blackjack([banker, player])
    game.init_game()

    window = GUI_init()
    window.mainloop()


if __name__ == "__main__":
    main()
