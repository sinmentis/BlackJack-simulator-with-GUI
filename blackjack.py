from tkinter import *

from decks import Decks
from player import Player

NUMBER_OF_DECK = 8


class Blackjack:
    def __init__(self, player_list):
        self.banker = player_list[0]
        self.player_list = player_list[0:]
        self.decks = None

    def init_game(self):
        self.decks = Decks(NUMBER_OF_DECK)
        self.decks.shuffle()
        print(f"New Blackjack started")
        print(self.decks)
