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

    @staticmethod
    def _rank_in(card_rank, rank_list):
        return any(card_rank == rank for rank in rank_list)

    def score_hand(self, aces_high):
        hand_sum = 0
        numbers = [str(n) for n in range(2, 11)]
        face_cards = list('JQK')
        for card in self._cards:
            if self._rank_in(card.rank, numbers):
                hand_sum += int(card.rank)
            elif self._rank_in(card.rank, face_cards):
                hand_sum += 10
            else:
                if aces_high:
                    hand_sum += 11
                else:
                    hand_sum += 1
        self._score = hand_sum
        return

    def get_cards(self):
        return copy.copy(self._cards)

    def __len__(self):
        return len(self._cards)

    @staticmethod
    def _card_string(card):
        return "Card(rank='{}',suit='{}')".format(card.rank, card.suit)

    def __str__(self):
        return ' '.join(map(self._card_string, self._cards))
