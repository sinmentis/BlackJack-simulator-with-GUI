from card import Card
from decks import Decks
from player import Player

NUMBER_OF_DECK = 8


def blackjack_value_rules(value: int) -> list:
    if value == 1:
        return [1, 11]
    else:
        return [min(value, 10), min(value, 10)]


class BlackjackPlayer(Player):
    def __init__(self, name, fund):
        Player.__init__(self, name, fund)
        self.has_insurance = False
        self.total_value = [0, 0]

    def ask_insurance(self):
        insurance_value = self.current_bet / 2
        if insurance_value > self.score:
            print(f"""
-------
Can't place insurance due to insufficient fund, current balance: {self.score}
-------
""")
            return
        enable = int(input(f"""
******
Insurance for {self.name}? it will be {insurance_value}
******
"""))
        if enable == 1:
            self.has_insurance = True
            self.score -= insurance_value
        return enable

    def ask_draw(self):
        # TODO: Implement special command like split / double-down / surrender
        one_more = int(input(f"""
******
{self.name} if need new card ? (0/1) 
current total number: {self.total_value}
current cards: {self.show_hand()}
******
"""))
        return one_more

    def add_card(self, card: Card):
        Player.add_card(self, card)
        self.total_value[0] += blackjack_value_rules(card.val)[0]
        self.total_value[1] += blackjack_value_rules(card.val)[1]

    def win(self):
        self.add_score(2)
        self.clear_hand()

    def lost(self):
        self.lose_score()
        self.clear_hand()

    def push(self):
        self.add_score(1)
        self.clear_hand()


class Blackjack:
    def __init__(self, player_list):
        self.banker = BlackjackPlayer(player_list[0].name, player_list[0].score)
        self.player_list = [BlackjackPlayer(player.name, player.score) for player in player_list[1:]]
        self.decks = None

    def init_game(self):
        self.decks = Decks(NUMBER_OF_DECK)
        self.decks.shuffle()
        print(f"New Blackjack started")
        print(self.decks)

    def prepare_players(self):
        for player in self.player_list:
            player.set_bet()

    def draw_first_two_card(self):
        for _ in range(2):
            for player in self.player_list:
                player.add_card(self.decks.draw())
            self.banker.add_card(self.decks.draw())

    def check_for_blackjack(self) -> set:
        def is_blackjack(x: BlackjackPlayer):
            return x.total_value[0] == 21 or x.total_value[1] == 21

        # If player has blackjack, pay the player straight away
        for player in self.player_list:
            if player.active and is_blackjack(player):
                print(f"""
******
Player {player.name} has a blackjack!
******
""")
                player.add_score(1.5)
                player.clear_hand()

        # Check for insurance if banker flashed is "A"
        if self.banker.hand[0].val == 1:
            [player.ask_insurance() for player in self.player_list]

        # If banker has blackjack, everybody loses
        if is_blackjack(self.banker):
            print(f"""
******
Banker has a blackjack!
******
""")
            for player in self.player_list:
                if player.active and player.has_insurance:
                    player.win(0.5)
                elif player.active:
                    player.lost()
        else:
            for player in self.player_list:
                if player.active and player.has_insurance:
                    player.has_insurance = False

    def player_decision_stage(self):
        for player in self.player_list:
            # Keep ask for draw if total value is less than 21
            while (player.total_value[0] < 21 or player.total_value[1] < 21) and len(player.hand) != 5:
                # Player instant win if more than 5 card without bust
                if player.total_value[0] > 21 and player.total_value[1] > 21:
                    player.lost()
                elif len(player.hand) == 5:
                    player.win()
                else:
                    one_more = player.ask_draw()
                    if one_more:
                        player.add_card(self.decks.draw())
                    else:
                        break
            else:
                continue

    def banker_decision_stage(self):
        # TODO: Implement hard 16 or soft 17
        while self.banker.total_value[0] < 17 or self.banker.total_value[1] < 17:
            self.banker.add_card(self.decks.draw())

    def check_player_against_banker(self):
        def get_total_score(total_value: list) -> int:
            if total_value[0] > 21 and total_value[1] > 21:
                result = 0
            elif total_value[0] > 21 and total_value[1] < 21:
                result = total_value[1]
            elif total_value[0] < 21 and total_value[1] > 21:
                result = total_value[0]
            else:
                result = max(total_value[0], total_value[1])
            return result

        # TODO: Implement banker push on 22

        # Go through player, win if total score greater than banker (close to 21)
        for player in self.player_list:
            if player.active:
                if get_total_score(player.total_value) < get_total_score(self.banker.total_value):
                    player.lost()
                elif get_total_score(player.total_value) == get_total_score(self.banker.total_value):
                    player.push()
                else:
                    player.win()

    def run_one_round(self):
        # Prepare Player - place bet
        self.prepare_players()

        # Deal two card to each player
        self.draw_first_two_card()

        # Check for user blackjack and insurance
        self.check_for_blackjack()

        # Player decision stage
        self.player_decision_stage()

        # Banker decision stage
        self.banker_decision_stage()

        # Check result
        self.check_player_against_banker()
