from hand import Hand
import copy
import collections
from dealer_player import DealerPlayer

Player = collections.namedtuple('Player', ['player_obj', 'hand', 'bank'])


class Dealer(DealerPlayer):

    def __init__(self, deck):
        self._deck = deck
        self._dealer = NotImplemented  # todo: what is this supposed to be?
        self._dealer_hand = Hand()
        self._players = dict()
        self.cards_dealt = list()

    def add_player(self, handle, player, player_bank):
        """
        takes Player and PlayerBank instances as parameters, does not return a value.
        It creates a new Hand instance and stores the three classes in the "players" data structure
        using the player's handle as the key. The method raises a RuntimeError if the player handle is
        already a key in the data structure
        """
        if handle in self._players:
            raise RuntimeError("player with same name already exists.")
        else:
            self._players[handle] = Player(player, Hand(), player_bank)

    def take_bets(self):
        """
        no parameters or return. Iterates through all players and calls their make_bet
        method, passing in their balance (since this is not stored in the player class). It then enters the
        bet into the PlayerBank object by calling the enter_bet method, passing in the player's bet.
        Raise a RuntimeError if a player's bet exceeds the player's balance
        """
        for handle, player in self._players.items():
            bet = player.player_obj.make_bet(player.bank.get_balance())
            player.bank.enter_bet(bet)

    def deal_initial_hand(self):
        """
        no parameters or return. Deals two cards from the deck to each player the cards are stored in the player's Hand
        instance with add_card. The cards are also stored in the cards_dealt list. The dealer also gets two cards,
        though the second card is dealt down, so it does not go in the cards_dealt list.
        """
        # deal to players
        for handle, player in self._players.items():
            for i in range(0, 2):
                card = self._deck.remove_card()
                player.hand.add_card(card)
                self.cards_dealt.append(card)
        # deal to yourself
        card = self._deck.remove_card()
        self._dealer_hand.add_card(card)
        self.cards_dealt.append(card)
        self._dealer_hand.add_card(self._deck.remove_card())

    def _apply_want_card(self, player):
        return player.player_obj.want_card(copy.deepcopy(player.hand),
                                 copy.deepcopy(player.bank),
                                 list(copy.deepcopy(self._dealer_hand[0])),
                                 copy.deepcopy(self.cards_dealt))

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
        for handle, player in self._players.items():
            want_card = self._apply_want_card(player)
            while want_card:
                # give player a card and add that to cards_dealt
                card = self._deck.remove_card()
                player.hand.add_card(card)
                self.cards_dealt.append(card)
                # see if they want to score their aces high or not
                aces_high = player.player_obj.use_ace_hi(copy.deepcopy(player.hand))
                # get their score and update it
                player.hand.score_hand(aces_high)
                score = player.hand.get_score()
                player.hand.set_score(score)
                # see if they've busted or not
                if score <= 21:
                    want_card = self._apply_want_card(player)
                else:
                    want_card = False

    def deal_dealer_hand(self):
        """
        no parameters or return. After the dealer has dealt to all players, she deals to herself. The dealer must follow
        specic rules and has no choices: must take cards until score is >= 17. Aces count as 11 unless the score goes
        over 21, then aces count low and dealer must take cards until her score is 17 or greater. The process is similar
        to the player deal. Be sure to update the dealer's hand and the cards_dealt list.
        """
        want_card = self.want_card(self._dealer_hand, None, None, None)
        while want_card:
            card = self._deck.remove_card()
            self._dealer_hand.add_card(card)
            self.cards_dealt.append(card)
            aces_high = self.use_ace_hi(self._dealer_hand)
            self._dealer_hand.score_hand(aces_high)
            score = self._dealer_hand.get_score()
            self._dealer_hand.set_score(score)
            if score <= 21:
                want_card = self.want_card(self._dealer_hand, None, None, None)
            else:
                want_card = False


    def settle_bets(self):
        """
        no parameters or return. After the dealer's hand is dealt, the scores are compared and bets are settled. If a player is bust
        they lose their wager. If a player is 21 or below, he wins if his score is greater than the dealer's
        score. Of course, if the dealer is bust (over 21) the player wins if he is below 21. A tie score with
        the dealer means the player loses. If a player wins, the dealer pays double her bet.
        The player's score is gotten from the Hand object and compared to the dealer's
        score. The PlayerBank methods pay_winner and bust are called to update the player's bank
        object.
        """
        for handle, player in self._players.items():
            dealer_score = self._dealer_hand.get_score()
            player_score = player.hand.get_score()
            if player_score > 21:
                player.bank.bust()
            elif player_score <= dealer_score and dealer_score <= 21 :
                player.bank.bust()
            else:
                player.bank.pay_winner(player.bank.get_wager()*2)

    def _get_player_summary(self, handle, hand, bank):
        return "Player: {}\nscore: {}\n{}\n{}\n".format(handle, hand.get_score(), str(hand), str(bank))

    def __str__(self):
        start_str = "$$$$$$  Game Summary  $$$$$$\n"
        dealer_str = "Dealer:\nscore: {}\n{}\n".format(self._dealer_hand.get_score(), str(self._dealer_hand))
        players = []
        for handle, player in self._players.items():
            players.append(self._get_player_summary(handle, player.hand, player.bank))
        players_str = '\n'.join(players)
        return '\n'.join([start_str, dealer_str, players_str])