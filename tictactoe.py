from tabulate import tabulate 
from random import choice

# Definition des Spielbretts als Dictionary; die keys sind die Feldernamen
# Die Feldnamen sind in der Form 'aij', wobei i für den Zeilenindex und j für den Spaltenindex steht
Spielbrett={'a11':'', 'a12':'', 'a13':'', 'a21':'', 'a22':'', 'a23':'', 'a31':'', 'a32':'', 'a33':''}

# Definition der Ausgabe des Spielbretts
def SpielbrettAusgabe(Spielbrett):
    Zeile1=[Spielbrett['a11'], Spielbrett['a12'], Spielbrett['a13']]
    Zeile2=[Spielbrett['a21'], Spielbrett['a22'], Spielbrett['a23']]
    Zeile3=[Spielbrett['a31'], Spielbrett['a32'], Spielbrett['a33']]
    print(tabulate([Zeile1, Zeile2, Zeile3], tablefmt='grid')) # tabulate erstellt eine schöne Tabelle als Spielfeld
    print('\n') # nach dem Spielfeld folgt eine  Leerzeile

# Jedem key (=Feld) des Dictionarys (=Spielbrett) wird dessen Name als value (=Eintrag) zugewiesen,
# um die Feldernamen anzuzeigen
def Feldernamen(Spielbrett):
    for feld in Spielbrett.keys():
        Spielbrett[feld]=feld

# leeres Spielfeld
def LeeresSpielbrett(Spielbrett):
    for feld in Spielbrett.keys():
        Spielbrett[feld]=' '

# Gewinnbedingungen
def Gewinn(Spielbrett):
    return( Spielbrett['a11']==Spielbrett['a12']==Spielbrett['a13'] !=' ' or # erste Zeile
            Spielbrett['a21']==Spielbrett['a22']==Spielbrett['a23'] !=' ' or # zweite Zeile
            Spielbrett['a31']==Spielbrett['a32']==Spielbrett['a33'] !=' ' or # dritte Zeile
            Spielbrett['a11']==Spielbrett['a21']==Spielbrett['a31'] !=' ' or # erste Spalte
            Spielbrett['a12']==Spielbrett['a22']==Spielbrett['a32'] !=' ' or # zweite Spalte
            Spielbrett['a13']==Spielbrett['a23']==Spielbrett['a33'] !=' ' or # dritte Spalte
            Spielbrett['a11']==Spielbrett['a22']==Spielbrett['a33'] !=' ' or # Hauptdiagonale
            Spielbrett['a13']==Spielbrett['a22']==Spielbrett['a31'] !=' '    # Nebendiagonale
            )

# volles Brett erkennen
def BrettVoll(Spielbrett):
    for feld in Spielbrett.keys():
        if Spielbrett[feld] == ' ':
            return False # sobald ein Feld noch leer ist, ist das Spielbrett noch nicht voll
    return True # wenn keines der Felder leer ist, ist das Spielbrett voll

# Das Spiel mit 2 Spielern
def TicTacToe2Spieler(Spielbrett):
    Feldernamen(Spielbrett)
    print('Die Felder des Spielbrettes haben folgende Bezeichnungen:')
    SpielbrettAusgabe(Spielbrett)
    LeeresSpielbrett(Spielbrett)
    Zug = 'X' # X beginnt
    while True:
        print(Zug + ' ist dran.') # Ausgabe, welcher Spieler an der Reihe ist
        Feld = input('Bitte das gewünschte Feld eingeben: ') # Input des gewünschten Feldes

        #Testen, ob der Input ein noch nicht belegtes Spielfeld ist
        if Feld in Spielbrett.keys():
            if Spielbrett[Feld] == ' ':
                Spielbrett[Feld] = Zug
            else:
                print('Dieses Feld ist bereits belegt.')
                continue
        else:
            print('Bitte ein valides Spielfeld eingeben.')
            continue

        SpielbrettAusgabe(Spielbrett)

        # Prüfen, ob das Spiel vorbei ist
        if Gewinn(Spielbrett) == True:
            print(Zug + ' hat gewonnen.')
            break
        elif BrettVoll(Spielbrett) == True:
            print('Unentschieden')
            break

        # Am Ende des Zuges wird auf den anderen Spieler gewechselt
        if Zug == 'X':
            Zug = 'O'
        else:
            Zug = 'X'

# Das Spiel gegen einen einfachen Computer
def TicTacToeGegenComputer(Spielbrett):
    Feldernamen(Spielbrett)
    print('Die Felder des Spielbrettes haben folgende Bezeichnungen:')
    SpielbrettAusgabe(Spielbrett)
    LeeresSpielbrett(Spielbrett)
    Zug = 'X' # X ist der Spieler, O der Computer
    while True:
        print(Zug + ' ist dran.') # Ausgabe, welcher Spieler an der Reihe ist
        if Zug == 'X':
            Feld = input('Bitte das gewünschte Feld eingeben: ') # Input des gewünschten Feldes
            #Testen, ob der Input ein noch nicht belegtes Spielfeld ist
            if Feld in Spielbrett.keys():
                if Spielbrett[Feld] == ' ':
                    Spielbrett[Feld] = Zug
                else:
                    print('Dieses Feld ist bereits belegt.')
                    continue
            else:
                print('Bitte ein valides Spielfeld eingeben.')
                continue
        elif Zug == 'O':
            # noch leere Felder in eine Liste schreiben
            moeglicheFelder = []
            for feld in Spielbrett.keys():
                if Spielbrett[feld] == ' ':
                    moeglicheFelder.append(feld)
            # Computer wählt zufälliges Feld aus dieser Liste aus und spielt seinen Zug
            Feld = choice(moeglicheFelder)
            Spielbrett[Feld] = Zug

        SpielbrettAusgabe(Spielbrett)

        # Prüfen, ob das Spiel vorbei ist
        if Gewinn(Spielbrett) == True:
            print(Zug + ' hat gewonnen.')
            break
        elif BrettVoll(Spielbrett) == True:
            print('Unentschieden')
            break

        # Am Ende des Zuges wird auf den anderen Spieler gewechselt
        if Zug == 'X':
            Zug = 'O'
        else:
            Zug = 'X'

# Das Spiel gegen einen unbesiegbaren Computer
def TicTacToeGegenMiniMax(Spielbrett):
    Feldernamen(Spielbrett)
    print('Die Felder des Spielbrettes haben folgende Bezeichnungen:')
    SpielbrettAusgabe(Spielbrett)
    LeeresSpielbrett(Spielbrett)
    Zug = 'X' # X ist der Spieler, O der Computer
    while True:
        print(Zug + ' ist dran.') # Ausgabe, welcher Spieler an der Reihe ist
        if Zug == 'X':
            Feld = input('Bitte das gewünschte Feld eingeben: ') # Input des gewünschten Feldes
            #Testen, ob der Input ein noch nicht belegtes Spielfeld ist
            if Feld in Spielbrett.keys():
                if Spielbrett[Feld] == ' ':
                    Spielbrett[Feld] = Zug
                else:
                    print('Dieses Feld ist bereits belegt.')
                    continue
            else:
                print('Bitte ein valides Spielfeld eingeben.')
                continue
        elif Zug == 'O':
            # Computer wählt besten Zug via MiniMax-Algorithmus
            besteBewertung = -100 # Computer versucht die Bewertung zu maximieren; daher wird ein sehr niedriger Initialwert gewählt
            besterZug = 'a' # a ist ein Platzhalter als Initiierung für den besten Zug
            # der Computer spielt jeden möglichen Zug und ermittelt für diesen eine Bewertung mittels MiniMax
            for feld in Spielbrett.keys():
                if Spielbrett[feld] == ' ':
                    Spielbrett[feld] = Zug
                    ZugBewertung = minimax(Spielbrett, False)
                    Spielbrett[feld] = ' '
                    # der Computer wählt den Zug mit der höchsten Bewertung, i.e. er maximiert
                    if ZugBewertung > besteBewertung:
                        besteBewertung = ZugBewertung
                        besterZug = feld
            # Computer spielt den ermittelten besten Zug
            Feld = besterZug
            Spielbrett[Feld] = Zug

        SpielbrettAusgabe(Spielbrett)

        # Prüfen, ob das Spiel vorbei ist
        if Gewinn(Spielbrett) == True:
            print(Zug + ' hat gewonnen.')
            break
        elif BrettVoll(Spielbrett) == True:
            print('Unentschieden')
            break

        # Am Ende des Zuges wird auf den anderen Spieler gewechselt
        if Zug == 'X':
            Zug = 'O'
        else:
            Zug = 'X'

# Hilfsfunktion für MiniMax
def WerGewinnt(Spielbrett, Zeichen):
    return( Spielbrett['a11']==Spielbrett['a12']==Spielbrett['a13'] == Zeichen or # erste Zeile
            Spielbrett['a21']==Spielbrett['a22']==Spielbrett['a23'] == Zeichen or # zweite Zeile
            Spielbrett['a31']==Spielbrett['a32']==Spielbrett['a33'] == Zeichen or # dritte Zeile
            Spielbrett['a11']==Spielbrett['a21']==Spielbrett['a31'] == Zeichen or # erste Spalte
            Spielbrett['a12']==Spielbrett['a22']==Spielbrett['a32'] == Zeichen or # zweite Spalte
            Spielbrett['a13']==Spielbrett['a23']==Spielbrett['a33'] == Zeichen or # dritte Spalte
            Spielbrett['a11']==Spielbrett['a22']==Spielbrett['a33'] == Zeichen or # Hauptdiagonale
            Spielbrett['a13']==Spielbrett['a22']==Spielbrett['a31'] == Zeichen    # Nebendiagonale
            )

# MiniMax-Funktion für den unbesiegbaren Computer
def minimax(Spielbrett, Maximieren):
    # erreicht die rekursive MiniMax-Funktion das Ende des Spiels, gib sie je einen entsprechenden Wert aus
    # gewinnt der Gegner des Computers, i.e. der Spieler, wird -1 ausgegeben.
    # der Computer maximiert, i.e. er will eine möglichst hohe Zugbewertung; daher ist dies für ihn die schlechteste Bewertung
    if WerGewinnt(Spielbrett, 'X') == True:
        return -1
    # ein Sieg für den Computer liefert das beste Ergebnis 1
    elif WerGewinnt(Spielbrett, 'O') == True:
        return 1
    # ein Unentschieden liefert 0; es ist für den Computer besser als zu verlieren, aber schlechter als zu gewinnen
    elif BrettVoll(Spielbrett) == True:
        return 0

    if Maximieren == True:
        besteBewertung = -100
        for feld in Spielbrett.keys():
            if Spielbrett[feld] == ' ':
                Spielbrett[feld] = 'O'
                ZugBewertung = minimax(Spielbrett, False)
                Spielbrett[feld] = ' '
                if ZugBewertung > besteBewertung:
                    besteBewertung = ZugBewertung
        return besteBewertung
    else:
        besteBewertung = 100
        for feld in Spielbrett.keys():
            if Spielbrett[feld] == ' ':
                Spielbrett[feld] = 'X'
                ZugBewertung = minimax(Spielbrett, True)
                Spielbrett[feld] = ' '
                if ZugBewertung < besteBewertung:
                    besteBewertung = ZugBewertung
        return besteBewertung

# Spielmenü mit Spielmodus-Auswahl und der Möglichkeit, mehrere Runden zu spielen
while True:
    print('Willkommen zu Tic-Tac-Toe!')
    print('Wähle einen Spielmodus\na = 2 Spieler; b = Spiel gegen einfachen Computer; c = Spiel gegen unbesiegbaren Computer')
    while True:
        Spielmodus = input('Spielmodus: ')
        if Spielmodus == 'a':
            TicTacToe2Spieler(Spielbrett)
            break
        elif Spielmodus == 'b':
            TicTacToeGegenComputer(Spielbrett)
            break
        elif Spielmodus == 'c':
            TicTacToeGegenMiniMax(Spielbrett)
            break
        else:
            print('Bitte validen Spielmodus auswählen.')
            continue
    while True:
        Weiterspielen = input('Noch eine Runde spielen? (j=ja, n=nein)')
        if Weiterspielen == 'n':
            print('Danke fürs Spielen!')
            break
        elif Weiterspielen == 'j':
            break
        else:
            print('Bitte \'j\' oder \'n\' eingeben.')
            continue
    if Weiterspielen == 'n':
        break