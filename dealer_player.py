class DealerPlayer:
    """
    After the dealer has dealt to all players, she deals to herself. The dealer must follow specic rules
    and has no choices: must take cards until score is >= 17. Aces count as 11 unless the score goes
    over 21, then aces count low and dealer must take cards until her score is 17 or greater."""

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
