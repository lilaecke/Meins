import random

def mixcards(n:int,Deck:list):
    '''mischt die Karten und verteilt sie abhängig von der Spielerzahl'''
    random.shuffle(Deck)
    returnDeck=[[],[],[],[],[],[],[],[]]
    i=0
    if n==2: z=12
    else: z=0
    while len(Deck)!=z:
        a,*b=Deck
        (returnDeck[i]).append(a)
        Deck=b
        i=(i+1)%n
    i=0
    '''while i<8:
        a,*b=returnDeck[i]#löscht das erste Element wieder
        returnDeck[i]=b
        i+=1'''
    if len(Deck)==0: return(None,returnDeck)
    else: return (Deck,returnDeck)

    
def carddeck():
    '''generiert einen sortierten CardDeck mit 32 Card'''
    deck=[]
    i=1
    while i<9:
        deck.append(("Pik",i));
        deck.append(("Herz",i))
        deck.append(("Karo",i))
        deck.append(("Kreuz",i))
        i+=1
    return deck



def deletequartet(Deck:list):
    '''schaut nach ob ein Wert im SpielerDeck mehrmals vorkommt und löscht ihn ggf'''
    names=[(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0)]
    i=0
    returner=False
    while i<len(Deck):
        a,b=Deck[i]
        c,d=names[b-1]
        d+=1
        names[b-1]=(c,d)
        i+=1
    for i in range(0,8):
        if names[i]==4:
            j=0
            while j<len(Deck):
                a,b=Deck[j]
                if b==i: Deck.remove((a,b))
                j+=1
    return Deck
    '''while i<4:
        a,b=names[i]
        j=1
        while j<9:
            k=0
            while k<len(Deck):
                if a=
                if (a,j)== Deck[k]: b+=1
                k+=1
            j+=1
        names[i]=(a,b)
        i+=1
        #bis hier wird gezählt wie oft was vorkommt, ab hier werden vierer gelöscht
    i=0
    while i<len(names):
        a,b=names[i]
        if b==4:
            returner=True
        i+=1
    return Deck,returner #returnt das Kartendeck + True/False je nachdem ob erfolgreich
'''
'''
deck=[]
#leer,deck=mixcards(3,carddeck())
deck=[('Karo', 1),('Karo', 2),('Karo', 3),('Karo', 4),('Pik', 3)]
print(deletequartet(deck))
print("as")'''
       

def drawcard(Card,Deck1:list,Deck2:list):
    '''Spieler 1 zieht von Spieler 2 Karte x. In der Rückgabe werden die beiden Decks
    + True oder False je nach Erfolg ausgegeben'''
    returner=False
    if Card in Deck2:
        Deck1.append(Card)
        Deck2.remove(Card)
        returner=True
    return (returner,Deck1,Deck2)

def checkifend(Deck1,Deck2):
    '''returnt True falls ein Deck fertig ist'''
    if (len(Deck1)==0) or (len(Deck2)==0): return (True)
    else: return (False)#wenn Spiel noch nicht beendet ist

def drawfromdeck(PlayerDeck,CardDeck):
    '''ziehe eine Karte vom Stapel und return Deck + Stapel'''
    if len(CardDeck)!=0:
        a,*b=CardDeck
        PlayerDeck=PlayerDeck+a

        CardDeck=b
    return (PlayerDeck,CardDeck)

def intinput(text):
    '''überprüft den Input gleichzeitig auf den Typ und wiederholt ggf die Aufforderung'''
    i=False
    while i==False:
        b=(input(text))
        if b.isdigit(): i=True
    return int(b)

def getcard():
    '''fragt die Karte ab und liefert das betreffende Tupel'''
    
    b=0
    a=""
    while a!="Pik" and a!="Herz" and a!="Karo" and a!="Kreuz":a=input("Kartenart: ")
    while b<1 or b>8: b=int(intinput("Nummer der Karte: "))    
    return (a,b)

def randomcard():
    i=random.randint(0,4)
    if i==0: a="Pik"
    elif i==1: a="Karo"
    elif i==2: a="Herz"
    elif i==3: a="Kreuz"

    i=random.randint(1,8)
    return (a,i)
