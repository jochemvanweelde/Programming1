import os
import sys
import time
infile = open('kluizen.txt', 'w+')
infile.write("Dit is een test")
kluizenAlle = 12  # Dit zijn alle kluizen die beschikbaar zijn
codeAan = True
while codeAan == True:

    def remove_empty_lines(filename):  # deze hele def is van het internet gehaalt en verwijdert lege regels.
        if not os.path.isfile(filename):
            print("{} does not exist ".format(filename))
            return
        with open(filename) as filehandle:
            lines = filehandle.readlines()

        with open(filename, 'w') as filehandle:
            lines = filter(lambda x: x.strip(), lines)
            filehandle.writelines(lines)


    def menu():
        print("==================================================================")
        print("1: Ik wil weten hoeveel kluizen er nog vrij zijn")
        print("2: Ik wil een nieuwe kluis")
        print("3: Ik wil even iets uit mijn kluis halen")
        print("4: Ik geef mijn kluis teruggeven")
        print("5: Annuleren en het programma stoppen")
        print("==================================================================")
        menuCijfer = int(input("Wat wilt u doen?:"))
        if menuCijfer < 1 or menuCijfer > 5:  # dit zorgt ervoor dat er een ERROR gegeven word als je een nummer die niet in het menu staat invoert
            print("ERROR: Geen geldig menu nummer.\nProbeer de nummers 1 tot en met 4")
        elif menuCijfer == 1:  # optie 1
            toon_aantal_kluizen_vrij()
        elif menuCijfer == 2:  # optie 2
            nieuwe_kluis()
        elif menuCijfer == 3:  # optie 3
            kluis_openen()
        elif menuCijfer == 4:  # optie 4
            kluis_teruggeven()
        else:  # optie 5
            annuleren()


    def toon_aantal_kluizen_vrij():
        kluizenBezet = sum(1 for line in open('kluizen.txt'))
        kluizenVrij = kluizenAlle - kluizenBezet + 1  # Omdat er een dertiende kluis is. Anders werkt mijn code niet
        print("Er zijn in totaal nog", kluizenVrij, "kluizen vrij")


    def nieuwe_kluis():
        kluizenBestand = infile.readlines()
        kluizenBestandList = []
        for kluizenBestandRegel in kluizenBestand:
            kluizenBestandSplit = kluizenBestandRegel.split(";")
            kluizenBestandList.append(int(kluizenBestandSplit[0]))  # De 0 zorgt ervoor dat alleen de kluisnummers in de list word gezet
        kluizenBestandList.sort()
        kluisNummer = 0
        for nummerCheck in kluizenBestandList:
            kluisNummer = kluisNummer + 1
            print(kluisNummer)
            print(nummerCheck)
            if nummerCheck != kluisNummer and kluisNummer <= kluizenAlle:
                print("Kluis", kluisNummer, "is beschikbaar!")
                wachtwoord = str(input("Geef een wachtwoord op, onthoud deze goed!:"))
                infile.write(str(kluisNummer))
                infile.write(';')
                infile.write(wachtwoord)
                infile.write('\n')
                print("Gelukt! kluis", kluisNummer, "is nu open en gaat automatisch op slot wanneer u de deur sluit")
                break
            if kluisNummer > kluizenAlle:
                print('Sorry, Alle kluizen zijn in gebruik')


    def kluis_openen():
        kluizenBestand = infile.readlines()
        kluizenBestandList = []
        for kluizenBestandRegel in kluizenBestand:
            kluizenBestandSplit = kluizenBestandRegel.split("\n")
            kluizenBestandList.append(
                kluizenBestandSplit[0])  # De 0 zorgt ervoor dat alleen de kluisnummers in de list word gezet
        invoerKluis = str(input('Wat is uw kluisnummer?:'))
        invoerWacthwoord = str(input('Wat is uw wachtwoord?:'))
        invoerTotaal = invoerKluis + ';' + invoerWacthwoord
        for nummer in range(1, len(kluizenBestand), 1):
            if invoerTotaal == kluizenBestandList[int(nummer)]:
                print("Gelukt! Uw kluis gaat nu open.")
                print("Je wachtwoord blijft opgeslagen en de kluis gaat op slot wanneer u de deur sluit")
                break
            elif nummer >= 12:
                print(
                    "Dat lijkt niet te kloppen! Misschien heeft u het verkeerde wachtwoord of kluisnummer ingevoerd. Probeer het nog een keer")


    def kluis_teruggeven():
        kluizenBestand = infile.readlines()
        invoerKluis = str(input('Wat is uw kluisnummer?:'))
        invoerWacthwoord = str(input('Wat is uw wachtwoord?:'))
        invoerTotaal = invoerKluis + ';' + invoerWacthwoord
        infile.seek(0)
        for nummer in kluizenBestand:
            if nummer != (invoerTotaal + '\n'):
                infile.write(nummer)
            else:
                print("Gelukt!")
        infile.write('\n\n\n')
        remove_empty_lines('kluizen.txt')


    def annuleren():
        sys.exit()

    nieuwe_kluis()
infile.close()