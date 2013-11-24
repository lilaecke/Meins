'''Funktionen'''

###Module
import sys
import os
from random import randint
from collections import Counter


#Kartensymbole
if sys.stdin.encoding.lower() == "cp850": ## Windoof console
    HEARTS, DIAMONDS, CLUBS, SPADES = '\x03', '\x04', '\x05', '\x06'
elif sys.stdin.encoding.lower() in ("utf-8", "cp1252"): ## Unix || IDLE
    HEARTS, DIAMONDS, CLUBS, SPADES = '\u2665', '\u2666', '\u2663', '\u2660'
else:
    HEARTS, DIAMONDS, CLUBS, SPADES = 'H', 'D', 'C', 'S'
H, D, C, S = HEARTS, DIAMONDS, CLUBS, SPADES


#Erstellen des Kartendecks
def create_deck():
    '''Deckerstellung'''
    deck = []
    symbol = [HEARTS,DIAMONDS,CLUBS,SPADES]
    for i in symbol:
        n = 0
        for j in range(8):
            n = n + 1
            card = (i,n)
            deck.append(card)
    return deck


#Bildschirm löschen
def clear():
    if os.name == "posix":
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        os.system("cls")
    else:
        print(80 * "\n")


#Anzeigenstrukturierung
def horizont():
    print(79 * "-")
    

#Unterprogramme - Spielablauf
def sort_cards(curr_hand):
    curr_hand.sort(key = lambda x: x[1])
    return curr_hand


def print_cards(curr_cardlist):
    '''Funktion zum kompaktes Anzeigen der Karten'''
    printlist = ""
    for i in curr_cardlist:
        card_temp = str(i[0]) + str(i[1])
        printlist += card_temp
        if i != curr_cardlist[-1]:
            printlist += ", "
    return printlist


def drop(curr_index, curr_hand, ki_comparelist, quartett_counter):
    '''Funktion zum Ablegen von Quartetten'''
    compare_list = []  
    for i in curr_hand:
        counter_temp = 0
        n = i[1]
        for j in curr_hand:
            if j[1] == n:
                counter_temp += 1
            else:
                pass
        if counter_temp == 4:
            compare_list.append(i)
        else:
            pass
    if compare_list != []:
        print("Folgende Karten wurden abgelegt:", print_cards(compare_list))
    for k in compare_list:
        curr_hand.remove(k)
        ki_comparelist.append(i)
        quartett_counter[curr_index].append(i)
    return curr_hand, ki_comparelist, quartett_counter


def ask_num_rl():
    '''Absturzsichere Abfrage: RL-Spielerzahl'''
    num_rl = input("Wie viele Realspieler spielen mit? ")
    while True:
        try:
            int(num_rl)
        except ValueError:
            num_rl = input("Bitte geben Sie eine Zahl ein: ")
            continue
        num_rl = int(num_rl)
        if 0 <= num_rl < 9:
            return num_rl
        else:
            num_rl = input("Bitte geben Sie eine Zahl zwischen 2 und 8 ein: ")


def ask_num_cp(rl):
    '''Absturzsichere Abfrage: CP-Spielerzahl'''
    num_cp = input("Wie viele Computerspieler sollen mitmachen? ")
    min_player = 2 - rl
    max_player = 8 - rl
    while True:
        try:
            int(num_cp)
        except ValueError:
            num_cp = input("Bitte geben Sie eine Zahl ein: ")
            continue
        num_cp = int(num_cp)
        if min_player <= num_cp <= max_player:
            return num_cp
        else:
            repeat_text = "Bitte geben Sie eine Zahl zwischen " + str(min_player) + " und " + str(max_player) + " ein: "
            num_cp = input(repeat_text)
            

def ask_enemy(curr_name, full_namelist, hands, quartett_counter):
    '''Absturzsichere Abfrage: Gegnername'''
    for i in range(len(hands)):
        print(full_namelist[i],"hat",len(hands[i]),"Karten und", len(quartett_counter[i]) // 4, "Quartetten.")
    while True:
        curr_enemy = input("Wen möchten Sie nach einer Karte fragen? ")
        if curr_enemy == curr_name:
            print("Du kannst dich nicht selbst fragen!")
            continue
        elif curr_enemy in full_namelist:
            print(curr_enemy,"ist dein Gegner!")
            return full_namelist.index(curr_enemy)
        else:
            print("Den Namen gibt es nicht!")


def ask_enemy_cp(full_namelist, hands):
    '''Gegnerabfrage von Computerspieler'''
    ki_comparelist = []
    for i in range(len(hands)):
        ki_comparelist.append(len(hands[i]))
    return ki_comparelist.index(max(ki_comparelist))


def ask_card():
    '''Absturzsichere Abfrage: Karte'''
    card = input("Nach welcher Karte soll gefragt werden? ")
    repeat = "Keine gültige Karte! Bitte geben Sie eine Karte ein: "
    acc_symbols = ("H","S","C","D")
    while True:
        try:
            int(card[1:])
        except ValueError:
            card = input(repeat)
            continue
        if card[0] not in acc_symbols:
            card = input(repeat)
        elif not 0 < int(card[1:]) < 9:
            card = input(repeat)
        else:
            return card


def check(asked_card, asked_enemy):
    '''Funktion zum Abfragen des Gegners'''
    card_temp = (eval(asked_card[0]), int(asked_card[1]))
    card_temp_display = str(card_temp[0]) + str(card_temp[1])
    if card_temp in asked_enemy:
        print("Treffer! Du hast", card_temp_display, "erhalten.")
        return card_temp
    else:
        print("Leider kein Treffer.")
        return 0


a = "CP1"
b = [(H,2),(H,3),(D,3),(S,3),(H,4),(H,5),(H,6)]
c = "CP2"
d = [(C,2),(C,5),(C,4),(D,5),(C,3)]
def check_cp(curr_name, curr_hand, enemy_name, enemy_hand):
    '''Kartenabfrage von Computerspieler'''
    compare_list = []  
    wished_quartett = []
    symbol_compare = [H, D, S, C]
    for i in curr_hand:
        compare_list.append(i[1])
    wished_card_num = Counter(compare_list).most_common()[0][0]
    for i in range(4):
        wished_quartett.append((symbol_compare[i],wished_card_num))
        if wished_quartett[i] not in curr_hand:
            wished_card = wished_quartett[i]
    wished_card_display = str(wished_card[0]) + str(wished_card[1])
    print(curr_name, "fragt", enemy_name, "nach", wished_card_display, "!")
    if wished_card in enemy_hand:
        print("Treffer!", curr_name, "hat", wished_card_display, "erhalten.")
        return wished_card
    else:
        print("Leider kein Treffer.")
        return 0
    
    

def win(hands, full_namelist, quartett_counter):
    '''Funktion zur Gewinnerermittlung'''
    winner = ""
    winner_list = []
    text_counter = 0
    if [] in hands:
        for i in range(len(quartett_counter)):
            winner_list.append(len(quartett_counter[i])) 
        if winner_list.count(max(winner_list)) == 1:
            print(full_namelist[winner_list.index(max(winner_list))], "hat gewonnen!")
        else:
            win_quart_num = max(winner_list)
            for i in winner_list:
                if i == win_quart_num:
                    winner += full_namelist[winner_list.index(i)]
                    text_counter += 1
                if text_counter != winner_list.count(max(winner_list)):
                    winner += ", "
            print(winner, "haben gewonnen!")
        print("Ergebnisse")
        for i in range(len(full_namelist)):
            print(full_namelist[i], ":", len(quartett_counter[i]) // 4, "Quartetten")
        return 1
    else:
        return 0

    
