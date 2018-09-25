def standaardprijs(afstandKM):
    if afstandKM <= 50 and afstandKM >= 0:
        bedrag = afstandKM * 0.8
    elif afstandKM < 0:
        bedrag = 0
    else:
        bedrag = 15 + afstandKM * 0.6
    return bedrag

def ritprijs(leeftijd, weekendrit, afstandKM):
    bedrag = standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == True:
            prijs = bedrag * 0.65
        else:
            prijs = bedrag * 0.7
    else:
        if weekendrit == True:
            prijs = bedrag * 0.6
        else:
            prijs = bedrag
    return prijs


print(float(ritprijs(20, False, 50)))