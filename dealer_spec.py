from dealer import Dealer
from french_deck import FrenchDeck
from conservative_player import ConservativePlayer
from player_bank import PlayerBank
from random_player import RandomPlayer


dealer = Dealer(FrenchDeck(123456))
dealer.add_player('conservative', ConservativePlayer(), PlayerBank(100))
dealer.add_player('random', RandomPlayer(), PlayerBank(100))
dealer.take_bets()
print("take bets\n\n")
print(str(dealer))
dealer.deal_initial_hand()
print("\n\ndeal initial hand\n\n")
print(str(dealer))
print(dealer.cards_dealt)
dealer.deal_player_hands()
print("\n\ndeal player hands\n\n")
print(str(dealer))
dealer.deal_dealer_hand()
print("\n\ndeal dealer hand\n\n")
print(str(dealer))
dealer.settle_bets()
print("\n\nsettle bets\n\n")
print(str(dealer))
