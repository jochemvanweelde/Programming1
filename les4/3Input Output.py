uurloon = input("Wat verdien jij per uur?:")
uur = input("Hoeveel uur heb jij gewerkt?:")
uurloonInt = float(uurloon)
uurInt = float(uur)
loon = round(uurloonInt * uurInt, 2)
print(uur, 'uur werken levert ', loon, ' Euro op!' )