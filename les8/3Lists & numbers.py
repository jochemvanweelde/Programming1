listNummer=[]
invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
listInvoer = [invoer]
for woord in listInvoer:
    listSplit = woord.split('-')
    listNummer.append(listSplit)
listNummer2 = max(listNummer)
results = list(map(int, listNummer2))
print("Gesorteerde list van ints: ", sorted(results))
print("Grootste getal: ", max(results), " en Kleinste getal: ", min(results))
print("Aantal getallen: ", len(results), " en Som van de getallen: ", sum(results))
print("Gemiddelde: ", (sum(results)/len(results)))