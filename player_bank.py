import copy


class PlayerBank:

    def __init__(self, balance):
        self._balance = balance
        self._bets_placed = 0
        self._is_winner = False

    def pay_winner(self, amount):
        """
        an amount passed in to be added to player's balance. Set is_winner to True.
        No return
        """
        self._balance += amount
        self._is_winner = True

    def bust(self):
         self._is_winner = False

    def get_balance(self):
        return copy.copy(self._balance)

    def get_wager(self):
        return copy.copy(self._bets_placed)

    def enter_bet(self, amount):
        if amount > self._balance:
            raise RuntimeError
        else:
            self._balance -= amount
            self._bets_placed += amount

    def __str__(self):
        return NotImplemented  # TODO
