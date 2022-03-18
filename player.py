class Player:
    def __init__(self, name, fund):
        self.name = name
        self.score = fund

        self.current_bet = 0
        self.hand = []
        self.active = True

    def set_bet(self):
        value = float(input(f"""{self.name} Please enter the bet unit: """))
        if self.score >= value:
            self.active = True
            self.current_bet = value
            self.score -= value
        else:
            while value > self.score:
                print(f"""
-------
Insufficient fund, current balance: {self.score}
-------
""")
                value = float(input(f"""{self.name} Please enter the bet unit: """))

    def add_score(self, factor):
        self.score += factor * self.current_bet
        print(f"""
******
{self.name} just won: {factor * self.current_bet}
******
""")

    def lose_score(self):
        self.score -= self.current_bet
        print(f"""
******
{self.name} just lost: {self.current_bet}
******
""")

    def add_card(self, card):
        self.hand.append(card)
        print(f"""
******
{self.name} received a new card
Current hand: {self.show_hand()}
******
""")

    def show_hand(self):
        template = ""
        for card in self.hand:
            template += f"\n\t{card.suit}: {card.val}"
        return template

    def clear_hand(self):
        self.hand = []
        self.active = False

    def __str__(self):
        template = f"""
=========
Player: {self.name}
Current Score: {self.score}
=========
"""
        return template
