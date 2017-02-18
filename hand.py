import copy


class Hand:

    def __init__(self):
        self._cards = list()
        self._score = 0

    def add_card(self, card):
        self._cards.append(card)

    def get_score(self):
        return copy.copy(self._score)

    def set_score(self, score):
        self._score = score

    def has_ace(self):
        return any(card.rank == "A" for card in self._cards)

    def score_hand(self, aces_high):
        # TODO
        return NotImplemented

    def get_cards(self):
        return copy.copy(self._cards)

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return "NotImplemented"
