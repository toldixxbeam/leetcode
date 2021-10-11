import sys
import pydealer
from bj_dict import card_values
import time

###New Hand
def new_hand():
    deck = pydealer.Deck()
    deck.shuffle()

    dealer = pydealer.Stack()
    dealer.add(deck.deal(2))

    player = pydealer.Stack()
    player.add(deck.deal(2))
   
    return dealer , player , deck


def dealer_check(dealer):
    dealer_blackjack = False
    dealer_hide = True
    if card_values['values'][dealer[0].value] == 10:
        print('Checking For Dealer Blackjack...')
        time.sleep(2)
        if dealer[1].value == 'Ace':
            dealer_hide = False
            dealer_blackjack = True
#            return dealer_blackjack , dealer_hide
        else:
            print('Continue...')
            print('---')
    if dealer[0].value == 'Ace':
        print('Insurance? Y/N')
        #insurance = input()
        if card_values['values'][dealer[1].value] == 10:
            print('Dealer Has Blackjack')
            dealer_hide = False
            dealer_blackjack = True
#            return dealer_blackjack , dealer_hide
    return dealer_blackjack , dealer_hide
