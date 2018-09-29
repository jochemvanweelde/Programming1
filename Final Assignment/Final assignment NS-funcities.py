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
jaar = int(input("Hoe oud ben jij?:"))
weekend = input("Rij jij in het weekend? (ja/nee)")
if weekend == 'ja':
    weekend == True
else:
    weekend == False
kilometer = int(input("Hoeveel kilometer is de reis?:"))
prijsRit = float(ritprijs(jaar, weekend, kilometer))
print("De reis kost voor jou precies ", prijsRit, " Euro!")