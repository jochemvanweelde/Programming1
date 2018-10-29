kluizenAlle = 12
def toon_aantal_kluizen_vrij(): #Dit geeft aan hoeveel kluizen er nog beschikbaar zijn
    kluizenBestand = open('kluizen.txt', 'r')
    kluizenBezet = sum(1 for line in kluizenBestand)
    kluizenBestand.close()
    kluizenVrij = kluizenAlle - kluizenBezet  # het verschil is gelijk aan hoeveel kluizen er nog beschikbaar zijn
    return kluizenVrij

def kluizen_lijst(): #Dit geeft alle nummers van de kluizen die bezet zijn
    kluizenBestand = open('kluizen.txt', 'r')
    kluizenLijst = []
    for kluizenBestandRegel in kluizenBestand:
        kluizenBestandSplit = kluizenBestandRegel.split(";")
        kluizenLijst.append(int(kluizenBestandSplit[0]))
    kluizenBestand.close()
    return kluizenLijst

def nieuwe_kluis(): #Hiermee registreer je een nieuwe kluis
    if toon_aantal_kluizen_vrij() > 0:
        kluizenLijst = kluizen_lijst()
        kluis = 0
        while True:
            kluis += 1
            if kluis not in kluizenLijst:
                print('Kluis', kluis, 'is beschikbaar')
                wachtwoord = input('Geef een wachtwoord op:')
                break
        kluizenSchrijven = open('kluizen.txt', 'a')
        kluizenSchrijven.write(str(kluis))
        kluizenSchrijven.write(';')
        kluizenSchrijven.write(wachtwoord)
        kluizenSchrijven.write('\n')
        kluizenSchrijven.close()
    else:
        return False

def kluis_openen(): #Hiermee open je een kluis maar verwijder je hem niet van de lijst
    vraagNummer = int(input('Welke kluis wil je openen?:'))
    if vraagNummer in kluizen_lijst():
        vraagWachtwoord = input('Oke! Vul nu het wachtwoord in:')
        textTotaal = str(vraagNummer)+';'+vraagWachtwoord
        kluizenBestand = open('kluizen.txt').read()
        if textTotaal in kluizenBestand:
            return textTotaal #Deze waarde komt bij kluis_teruggeven van pas
        else:
            return False
    else:
        return False

def kluizen_lijst2(): #Dit is een lijst met nummers en wachtwoorden met een puntkomma ertussen (1;test\n)
    kluizenBestand = open('kluizen.txt', 'r')
    kluizenLijst2 = []
    for kluizenBestandRegel in kluizenBestand:
        kluizenLijst2.append(kluizenBestandRegel)
    kluizenBestand.close()
    return kluizenLijst2

def kluis_teruggeven(): #Hiermee verwijder je een kluis uit het bestand zodat er weer een plekje vrij komt
    kluizenLijst = kluizen_lijst2()
    print(kluizenLijst)
    text = kluis_openen()
    for kluisline in kluizenLijst:
        if text in kluisline:
            kluizenLijst.remove(kluisline)
            with open('kluizen.txt', 'w') as f:
                for item in kluizenLijst:
                    f.write("%s" % item)
                f.close()
                return True
    return False


while True:
    print("==================================================================")
    print("1: Ik wil weten hoeveel kluizen er nog vrij zijn")
    print("2: Ik wil een nieuwe kluis")
    print("3: Ik wil even iets uit mijn kluis halen")
    print("4: Ik geef mijn kluis teruggeven")
    print("5: Annuleren en het programma stoppen")
    print("==================================================================")
    menuCijfer = str(input("Wat wilt u doen?:"))
    if menuCijfer == '1':  # optie 1
        print('Er zijn nog', toon_aantal_kluizen_vrij(), 'kluizen vrij')
    elif menuCijfer == '2':  # optie 2
        if nieuwe_kluis():
            print('Gelukt')
        else:
            print('Er is geen kluis vrij')
    elif menuCijfer == '3':  # optie 3
        if kluis_openen():
            print('Gelukt! Je kluis is nu open')
        else:
            print('Het lijkt er op dat er iets mis is gegaan')
    elif menuCijfer == '4':  # optie 4
        if kluis_teruggeven():
            print('Gelukt! LET OP! Hierna kan je niet meer terug in je kluis')
        else:
            print('Het lijkt erop dat er iets mis is gegaan')
    else:  # optie 5
        print('ONGELDIGE INPUT! CODE ONDERBROKEN')
        break