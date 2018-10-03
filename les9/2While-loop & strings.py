while True:
    vraagWoord = input("Geef een string van vier letters:")
    if len(vraagWoord) == 4:
        break
    else:
        print("Ehm... Nee dat lijkt niet te kloppen", vraagWoord, "heeft", len(vraagWoord), "letters. Probeer het nog een keer!")
print("Ja!", vraagWoord, "Heeft inderdaad vier letters. Gelukt!")