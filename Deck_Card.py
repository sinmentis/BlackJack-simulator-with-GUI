# -*- coding:utf-8 -*-
import random


class Deck:
    def __init__(self, joker=False):
        self.cards = []
        self.build(joker) if joker else self.build()

    def build(self, joker=False):
        for card_suit in ["Spade", "Club", "Diamond", "Heart"]:
            for card_val in range(1, 14):
                self.cards.append(Card(card_suit, card_val))
        if joker:
            self.cards.append(Card("Joker", 15))
            self.cards.append(Card("Joker", 16))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop(random.randint(0, len(self.cards)-1))


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def __str__(self):
        return "Suit: {0:^8}| Value: {1:^7} |".format(self.suit, self.val)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def get_card(self, card):
        self.hand.append(card)

    def lose_card(self, index):
        return self.hand.pop(index)

    def show_hand(self):
        for card in self.hand:
            print(card)
