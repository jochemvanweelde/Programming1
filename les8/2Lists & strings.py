listVierLetter=[]
invoerList = eval(input("Geef lijst met minimaal 10 strings: "))
for woord in invoerList:
    if len(woord) == 4:
        listVierLetter.append(woord)
print("De nieuw-gemaakte lijst met alle vier-letter strings is: \n", listVierLetter)
