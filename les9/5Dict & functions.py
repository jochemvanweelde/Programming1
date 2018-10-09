dict = {}
def namen():
    while True:
        invoerNaam = input("Geef een naam op: ")
        if invoerNaam == "":
            print(dict, "Geen naam gevonden programma word gestopt")
            break
        else:
            dict[invoerNaam] = invoerNaam

namen()