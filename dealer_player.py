class DealerPlayer:

    def make_bet(self, balance):
        return 0

    def use_ace_hi(self, hand):
        aces_high = True
        hand.score_hand(aces_high)
        if hand.get_score() > 21:
            aces_high = False
        return aces_high

    def want_card(self, hand, bank, dealer_hand, cards_dealt):
        return hand.get_score() < 17
