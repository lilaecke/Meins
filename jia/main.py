'''Hauptprogramm'''

#Laden der Module
import sys
from random import randint
from random import shuffle
from functions import create_deck
from functions import clear
from functions import horizont
from functions import sort_cards
from functions import print_cards
from functions import drop
from functions import ask_num_rl
from functions import ask_num_cp
from functions import ask_enemy
from functions import ask_enemy_cp
from functions import ask_card
from functions import check
from functions import check_cp
from functions import win


#Kartensymbole
if sys.stdin.encoding.lower() == "cp850": ## Windoof console
    HEARTS, DIAMONDS, CLUBS, SPADES = '\x03', '\x04', '\x05', '\x06'
elif sys.stdin.encoding.lower() in ("utf-8", "cp1252"): ## Unix || IDLE
    HEARTS, DIAMONDS, CLUBS, SPADES = '\u2665', '\u2666', '\u2663', '\u2660'
else:
    HEARTS, DIAMONDS, CLUBS, SPADES = 'H', 'D', 'C', 'S'
H, D, C, S = HEARTS, DIAMONDS, CLUBS, SPADES


#Spielausführung / Restart
def restart(x):
    global quartett
    if x == "Neustart":
        quartett()
    else:
        return x

def myinput(question):
    q = input(question)
    if q == "restart" ...
    if q == "exit" ...


def quartett():
    #Deckerstellung
    deck = create_deck()

    #KI-Hilfskomponenten
    ki_comparelist = deck.copy()

    #Ausführung des Programms
    #Namen und Anzahl der Spieler
    rl_namelist = []
    cp_namelist = []
    full_namelist = []

    num_rl = ask_num_rl()
    num_cp = ask_num_cp(num_rl)
    num_full = num_rl + num_cp

    quartett_counter = []

    for i in range(num_rl):
        rl_namequestion = "Wie heißt Spieler "+str(i+1)+"? "
        rl_name_temp = restart(input(rl_namequestion))
        while rl_name_temp == " ":
            rl_name_temp = restart(input("Keine gültige Eingabe! Bitte geben Sie einen Namen ein: "))
        while rl_name_temp in rl_namelist:
            rl_name_temp = restart(input("Der Spielername ist vergeben! Bitte wähle einen anderen Namen: "))
        rl_namelist.append(rl_name_temp)
        full_namelist.append(rl_name_temp)

    for i in range(num_cp):
        cp_name_temp = "CP"+str(i+1)
        cp_namelist.append(cp_name_temp)
        full_namelist.append(cp_name_temp)

    horizont()
    print("Spielteilnehmer:")
    for i in range(len(full_namelist)):
        print(full_namelist[i])

    for i in range(num_full):
        quartett_counter.append([])

    #Verteilen der Karten
    hands = []
    for i in range(num_full):
        hands.append([])

    if num_full == 2:
        for i in range(2):
            for j in range(10):
                curr_card = deck[randint(0,len(deck) - 1)]
                deck.remove(curr_card)
                hands[i-1].append(curr_card)
    else:
        curr_player_index = 0
        while len(deck) > 0:
            curr_card = deck[randint(0,len(deck) - 1)]
            deck.remove(curr_card)
            hands[curr_player_index].append(curr_card)
            curr_player_index += 1
            if curr_player_index == num_full:
                curr_player_index = 0
            else:
                pass

    #Spielablauf
    curr_index = 0
    game = 0

    horizont()
    print("Das Spiel fängt an!")
    horizont()
    while game == 0:
        curr_name = full_namelist[curr_index]
        curr_hand = sort_cards(hands[curr_index])
        print(curr_name,"ist dran!")
        restart(input("Drücke eine Taste um fortzufahren."))
        if curr_name in rl_namelist:        
            clear()
            horizont()
            print("Deine Hand:", print_cards(curr_hand))
            curr_hand, ki_comparelist, quartett_counter = drop(curr_index, curr_hand, ki_comparelist, quartett_counter)
            game += win(hands, full_namelist, quartett_counter)
            while game == 0:
                if num_full == 2:
                    enemy_index = curr_index + 1
                    if enemy_index == 2:
                        enemy_index = 0
                    for i in range(len(hands)):
                        print(full_namelist[i],"hat",len(hands[i]),"Karten und", len(quartett_counter[i]) // 4, "Quartetten.")
                else:
                    enemy_index = ask_enemy(curr_name, full_namelist, hands, quartett_counter)
                enemy_hand = hands[enemy_index]
                wished_card = ask_card()
                wished_card = check(wished_card, enemy_hand)
                if wished_card == 0:
                    if len(deck) > 0:
                        card_draw = deck.pop()
                        curr_hand.append(card_draw)
                        print("Du hast",print_cards([card_draw]),"gezogen.")
                        curr_hand, ki_comparelist, quartett_counter = drop(curr_index, curr_hand, ki_comparelist, quartett_counter)
                        game += win(hands, full_namelist, quartett_counter)
                    break
                else:
                    curr_hand.append(wished_card)
                    enemy_hand.remove(wished_card)
                    curr_hand, ki_comparelist, quartett_counter = drop(curr_index, curr_hand, ki_comparelist, quartett_counter)
                    game += win(hands, full_namelist, quartett_counter)
                    if game != 0:
                        break
                    horizont()
                    print("Deine Hand:", print_cards(sort_cards(curr_hand)))
            if game != 0:
                break
            input("Drücke eine Taste um Zug zu beenden.")
            clear()
        else:
            horizont()
            curr_hand, ki_comparelist, quartett_counter = drop(curr_index, curr_hand, ki_comparelist, quartett_counter)
            win(hands, full_namelist, quartett_counter)
            if num_full == 2:
                enemy_index = curr_index + 1
                if enemy_index == 2:
                    enemy_index = 0
            else:
                enemy_index = ask_enemy_cp(full_namelist, hands)
            enemy_hand = hands[enemy_index]
            enemy_name = full_namelist[enemy_index]
            while game == 0:
                wished_card = check_cp(curr_name, curr_hand, enemy_name, enemy_hand)
                if wished_card == 0:
                    if len(deck) > 0:
                        card_draw = deck.pop()
                        curr_hand.append(card_draw)
                        print(curr_name, "hat eine Karte gezogen.")
                        curr_hand, ki_comparelist, quartett_counter = drop(curr_index, curr_hand, ki_comparelist, quartett_counter)
                        game += win(hands, full_namelist, quartett_counter)
                    break
                else:
                    curr_hand.append(wished_card)
                    enemy_hand.remove(wished_card)
                    curr_hand, ki_comparelist, quartett_counter = drop(curr_index, curr_hand, ki_comparelist, quartett_counter)
                    game += win(hands, full_namelist, quartett_counter)
                    if game != 0:
                        break
                if game != 0:
                    break
        curr_index += 1
        if curr_index == len(full_namelist):
            curr_index = 0

quartett()
