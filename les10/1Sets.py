treinBruin = {"Deurne", "Helmond Brouwhuis", "Helmond", "Helmond 't Hout", "Eindhoven", "Beukenlaan", "Best", "Boxtel"}
treinGroen = {"Weert", "Heeze", "Geldrop", "Eindhoven", "Beukenlaan", "Best", "Boxtel"}
treinOvereenkomst = treinBruin.intersection(treinGroen)
treinBruinVerschil = treinBruin.difference(treinGroen)
alleStations = treinBruinVerschil, treinGroen
print(treinOvereenkomst)
print(treinBruinVerschil)
print(alleStations)