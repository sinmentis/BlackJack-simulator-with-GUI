class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []

    def get_card(self, card):
        self.hand.append(card)

    def lose_card(self, index):
        return self.hand.pop(index)

    def show_hand(self):
        for card in self.hand:
            print(card)
