class Card:
    def __init__(self, suit: str, val: int):
        self.suit = suit
        self.val = val

    def __str__(self) -> str:
        return "Suit: {0:^8}| Value: {1:^7} |".format(self.suit, self.val)
