import pydealer
import time

from bj_dict import card_values


deck = pydealer.Deck()
deck.shuffle()


player = pydealer.Stack()
player.add(deck.deal(2))

dealer = pydealer.Stack()
dealer.add(deck.deal(2))

print(f'Player: \n{player} \n \n')
print(f'Dealer: \n{dealer}')
print('-------------------------')



print(f'Dealer Shows {dealer[0].value} of {dealer[0].suit}')
print('---')
###Check For Dealer Blackjack
if card_values['values'][dealer[0].value] == 10:
    print('Checking For Dealer Blackjack...')
    time.sleep(2)
    if dealer[1].value == 'Ace':
        print('Dealer Has Blackjack')
    else:
        print('Continue...')
        print('---')
if dealer[0].value == 'Ace':
    print('Insurance? Y/N')
    insurance = input()
    


def player_hand():
    global bust
    bust = False
    global blackjack
    blackjack = False
    global player_count
    player_count = 0
    for cards in player:
        if cards.value != 'Ace':
            value = card_values['values'][cards.value]
            print(f'Player Shows {cards.value} of {cards.suit} | ({value}) |')
            player_count = player_count+value
    for cards in player:
        if cards.value == 'Ace':
            if player_count+11 <= 21:
                value = 11
            else:
                value = 1
            print(f'Player Shows {cards.value} of {cards.suit} | ({value}) |')
            player_count = player_count+value
    if player_count > 21:
        print(f'Player Bust ({player_count})... Game Over.')
        bust = True
    if player_count == 21:
        print(f'Player Has Blackjack!')
        blackjack = True

    return player_count


while player_hand() < 21:
    hit_stay = input(f'Player Has {player_count}. \nHit? Y/N: \n')
    if hit_stay == 'Y':
        player.add(deck.deal())
    elif hit_stay == 'N':
        break
    else:
        print('Not a Valid Entry. Please Enter Y/N')



def dealer_hand():
    global dealer_count
    dealer_count = 0
    for cards in dealer:
        if cards.value != 'Ace':
            value = card_values['values'][cards.value]
            print(f'Dealer Shows {cards.value} of {cards.suit} | ({value}) |')
            dealer_count = dealer_count+value
    for cards in dealer:
        if cards.value == 'Ace':
            if dealer_count+11 <= 21:
                value = 11
            else:
                value = 1
            dealer_count = dealer_count+value
    print(f'Dealer has {dealer_count}')
    return dealer_count

while dealer_hand() < 17:
    if not blackjack:
        dealer.add(deck.deal())

if dealer_count > 21:
    print(f'Dealer Bust! Player Wins')
elif dealer_count > player_count:
    print(f'Dealer Wins with {dealer_count}')
elif dealer_count < player_count:
    if bust != True:
        print(f'Player Wins with {player_count}')
    



