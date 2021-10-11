import PySimpleGUI as sg
import time
import pydealer

from bj_dict import card_values
from bj_functions import new_hand

test_cards = [ [sg.Image(filename='cards/back.png'),sg.Image(filename='cards/back.png')]]


player_cards = [[sg.Image(filename=None),sg.Image(filename=None)]]
player_hand = player_cards

dealer_cards = [[sg.Image(filename=None),sg.Image(filename=None)]]
dealer_hand = dealer_cards
#card_template = "sg.Image(filename='cards/"+card+".png')"
#player_cards = [[]]

def card_pic(card):
    value = card_values['file_value'][card.value]
    suit = card_values['file_suit'][card.suit]
    card = "cards/"+value+"_"+suit+".png"
    
    return card
    


layout = [ 
           [sg.Frame("Dealer's Hand", dealer_cards)],
           [sg.Frame("Player's Hand", player_cards)],
           [sg.Button('Deal New Hand')] ]



#event, values = sg.Window('Marlon Blackjack', layout).read(close=True)

window = sg.Window('Marlon Blackjack', layout)


while True:

    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Deal New Hand':

        def new_hand():
            deck = pydealer.Deck()
            deck.shuffle()
            dealer = pydealer.Stack()
            dealer.add(deck.deal(2))
            player = pydealer.Stack()
            player.add(deck.deal(2))        
            return dealer , player , deck
        
        new_hand = new_hand()
        dealer = new_hand[0]
        dealer_hand[0][0].Update(card_pic(dealer[0]))
        dealer_hand[0][1].Update(card_pic(dealer[1]))
        
        player = new_hand[1]
        player_hand[0][0].Update(card_pic(player[0]))
        player_hand[0][1].Update(card_pic(player[1]))
        
        time.sleep(1)
        

    if event == 'Marlon':
        player_card_one,player_card_two = card_pic(player[0]),card_pic(player[1])
        
        player_hand[0][0].Update(player_card_one)
        player_hand[0][1].Update(player_card_two)
        
