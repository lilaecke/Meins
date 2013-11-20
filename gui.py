from sys import exit
from random import shuffle
from time import sleep
from impl import mixcards
from impl import carddeck
from impl import deletequartet
from impl import drawcard
from impl import checkifend
from impl import drawfromdeck
from impl import intinput
from impl import getcard
from impl import randomcard
from pprint import pprint


player = []
n = 0

def player():
    n=0
    while n > 8 or n < 2:
        n=int(intinput("Geben Sie die Spieleranzahl an: "))
        if n < 2 or n > 8:
            print ("Bitte geben Sie eine Zahl zwischen 2 und 8 an")
    c=-1
    while c > n or c < 0:
        c=int(intinput("Geben Sie die Anzahl der nicht Computergegner an: "))
        if c > n or c <0:
            print ("Bitte geben Sie eine Zahl zwischen 2 und 8 an")

    i=0
    player_list = []
   
    while i < c:
       a = input("Gebe Spielernamen ein: ")
       player_list.append((a,True))
       i += 1
    while i < n:
        player_list.append((i,False))
        i += 1
    return player_list


deck=[]
player_list = player()
deck, card_list = mixcards(len(player_list), carddeck())
whoseturn = 0 #wer ist dran, aktueller Spieler
enemy = -5 #Gegner, von dem gezogen wird
#print(card_list)
while True:
    card_list[whoseturn]
    card_list_tmp = sorted(card_list[whoseturn], key=lambda x: x[1])
    pprint(card_list_tmp)
    if len(player_list) != 2:
        while enemy < 0 or enemy > len(player_list) or enemy == whoseturn:
            enemy=intinput ("Von wem möchten Sie eine Karte ziehen? ")
    else: enemy = (whoseturn + 1) % 2 # Spieler 2 automatisch Gegner (bei 2 Spielern)
    card_list[enemy]

    card_list_tmp = sorted(card_list[enemy], key=lambda x: x[1])

    print("Gegner:")
    pprint(card_list_tmp)
    wantcard = getcard() # welche Karte gewünscht?
    success, card_list[whoseturn], card_list[enemy] = \
             drawcard(wantcard, card_list[whoseturn], card_list[enemy])
#zeilenlänge noch anpassen!!--------------------------------------------
    if success: print("Karte erfolgreich vom Gegner gemopst")
    else: print("Dein Gegner hat diese Karte nicht")
    
    card_list[whoseturn] = deletequartet(card_list[whoseturn])
    if checkifend(card_list[whoseturn], card_list[enemy]): exit()
    if not success:
        card_list[whoseturn], deck = drawfromdeck(card_list[whoseturn], deck)
        whoseturn = (whoseturn + 1) % len(player_list)
print(success)








        
    
