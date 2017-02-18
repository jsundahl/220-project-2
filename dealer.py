from hand import Hand
import collections

Player = collections.namedtuple('Player', ['player_obj', 'hand', 'bank'])


class Dealer:

    def __init__(self, deck):
        self._deck = deck
        self._dealer = NotImplemented
        self._dealer_hand = NotImplemented
        self._players = dict()
        self.cards_dealt = NotImplemented

    def add_player(self, handle, player, player_bank):
        """
        takes Player and PlayerBank instances as parameters, does not return a value.
        It creates a new Hand instance and stores the three classes in the "players" data structure
        using the player's handle as the key. The method raises a RuntimeError if the player handle is
        already a key in the data structure
        """
        if self._players[handle] is not None:
            raise RuntimeError("player with same name already exists.")
        else:
            self._players[handle] = Player(player, Hand(), player_bank)
        return

    def take_bets(self):
        """
        no parameters or return. Iterates through all players and calls their make_bet
        method, passing in their balance (since this is not stored in the player class). It then enters the
        bet into the PlayerBank object by calling the enter_bet method, passing in the player's bet.
        Raise a RuntimeError if a player's bet exceeds the player's balance
        """
        return NotImplemented

    def deal_initial_hand(self):
        """
        no parameters or return. Deals two cards from the deck to each playerthe cards are stored in the player's Hand instance with add_card. The cards are also stored in
        the cards_dealt list. The dealer also gets two cards, though the second card is dealt down, so
        it does not go in the cards_dealt list.
        """
        return

    def deal_player_hands(self):
        """
        no parameters or return. This method implements the rules described
        above in the Dealing to Players section. Each player is asked if it wants a card and if it wants to
        calculate the score using ace high or low. The Player methods are want_card and use_ace_hi.
        The dealer passes copies of the required data to the player (see Player interface). The dealer
        updates the player's hand with the score after the player is processed, i.e. has stopped taking
        cards or has bust. Remember that only the dealer can update a player's hand with cards and
        score. Remember that all cards dealt should be added to the cards_dealt list
        """
        return

    def deal_dealer_hand(self):
        """
        no parameters or return. This method implements the rules described
        in the Dealer Deal section above. The process is similar to the player deal. Be sure to update
        the dealer's hand and the cards_dealt list.
        """
        return

    def settle_bets(self):
        """
        no parameters or return. Implements the rules described in the Settle Bets
        section above. The player's score is gotten from the Hand object and compared to the dealer's
        score. The PlayerBank methods pay_winner and bust are called to update the player's bank
        object.
        """
        return

    def __str__(self):
        return NotImplemented
