class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def __str__(self):
        return "Suit: {0:^8}| Value: {1:^7} |".format(self.suit, self.val)
