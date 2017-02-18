import random


class RandomPlayer:


    def make_bet(self, balance):
        return random.randrange(0, balance + 1)

    def use_ace_hi(self, hand):
        return random.randrange(0,2) == 0

    def want_card(self, hand, bank, dealer_hand, cards_dealt):
        return random.randrange(0, 2) == 0
