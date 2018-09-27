som = []
def gemiddelde():
    vraag = input("Voer een willekeurige zin in:")
    list = vraag.split()
    for woord in list:
        som.append(len(woord))
    print(sum(som)/len(som))
gemiddelde()