import copy


class PlayerBank:

    def __init__(self, balance):
        self._balance = balance
        self._bets_placed = 0
        self._is_winner = False

    def pay_winner(self, amount):
        self._balance += amount
        self._is_winner = True

    def bust(self):
        self._bets_placed = 0
        self._is_winner = False

    def get_balance(self):
        return copy.copy(self._balance)

    def get_wager(self):
        return copy.copy(self._bets_placed)

    def enter_bet(self, amount):
        if amount > self._balance:
            raise RuntimeError("Bet greater than balance")
        else:
            self._balance -= amount
            self._bets_placed += amount

    def __str__(self):
        win_status = ""
        if self._is_winner:
            win_status = "winner!"
        else:
            win_status = "bust."
        return "Player assets:\nbet {} balance {} {}".format(self._bets_placed, self._balance, win_status)
