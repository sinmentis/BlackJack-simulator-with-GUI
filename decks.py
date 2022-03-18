# -*- coding:utf-8 -*-
import random
from card import Card


class Decks:
    def __init__(self, number_of_deck=1, joker=False):
        self.available_cards = []
        self.abandon_cards = []
        self.number_of_deck = number_of_deck
        self.build_new_deck(self.number_of_deck, joker)

    def build_new_deck(self, number_of_deck, joker):
        self.available_cards = []
        self.abandon_cards = []
        for card_suit in ["Spade", "Club", "Diamond", "Heart"]:
            for card_val in range(1, 14):
                self.available_cards.append(Card(card_suit, card_val))
        if joker:
            self.available_cards.append(Card("Joker", 15))
            self.available_cards.append(Card("Joker", 16))

        self.available_cards = number_of_deck * self.available_cards

    def shuffle(self):
        for i in range(len(self.available_cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.available_cards[i], self.available_cards[r] = self.available_cards[r], self.available_cards[i]

    def draw(self):
        # Get random card
        random_card_index = random.randint(0, len(self.available_cards) - 1)
        random_card = self.available_cards[random_card_index]

        # Add to abandon card container, remove from available
        self.abandon_cards.append(random_card)
        self.available_cards.pop(random_card_index)

        return random_card

    def __str__(self):
        template = f"""Total Deck: {self.number_of_deck}
        current available card: {len(self.available_cards)}
        current abandoned card: {len(self.abandon_cards)}"""

        return template
