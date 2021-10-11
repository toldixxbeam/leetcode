import pygame
from pygame.locals import *

import os
import time
import sys
import pydealer
from bj_dict import card_values
from bj_functions import new_hand , dealer_check


pygame.init()
width, height = 600, 400
screen = pygame.display.set_mode((width, height))

draw_card = False
dealer_hide = True

background = pygame.image.load("png/bj_back.png")


pygame.display.set_caption('Blackjack')

while True:

  
    
    # 5 - clear the screen before drawing it again
    screen.fill(0)
#    screen.fill((60,25,60))
    # 6 - draw the screen elements
    screen.blit(background, (0,0))
    # 7 - update the screen
#    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)

        if event.type==pygame.KEYDOWN:
            # if it is quit the game
            if event.key == K_ESCAPE:
                pygame.quit() 
                exit(0)

                
###Start new Hand
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                deal = new_hand()
                player = deal[1]
                dealer = deal[0]
                print(f'Player: \n{player} \n \nDealer: \n{dealer}')
                draw_card = deal[2]
                time.sleep(2)
                dealer_bj = dealer_check(dealer)
                dealer_hide = dealer_bj[1]
                dealer_blackjack = dealer_bj[0]

    if draw_card == True:

        if dealer_hide == True:
            w_d,h_d = 250,0
            for hand in dealer[0:1]:
                value,suit = card_values["file_value"][hand.value],card_values["file_suit"][hand.suit]
                card = 'cards/' + value + '_' + suit + '.png'
                player_cards = pygame.image.load(card)
                screen.blit(pygame.image.load('cards/back.png'),(w_d,h_d))
                w_d = w_d+12
                screen.blit(player_cards,(w_d,h_d))


        if dealer_bj == True:
            w_d,h_d = 262,0
            for hand in dealer:
                value,suit = card_values["file_value"][hand.value],card_values["file_suit"][hand.suit]
                card = 'cards/' + value + '_' + suit + '.png'
                player_cards = pygame.image.load(card)
                screen.blit(player_cards,(w_d,h_d))
                w_d = w_d+12

        w_p,h_p = 250,250
        for hand in player:
            value,suit = card_values["file_value"][hand.value],card_values["file_suit"][hand.suit]
            card = 'cards/' + value + '_' + suit + '.png'
            player_cards = pygame.image.load(card)
            screen.blit(player_cards,(w_p,h_p))
            w_p = w_p +12            

    

    pygame.display.update()

