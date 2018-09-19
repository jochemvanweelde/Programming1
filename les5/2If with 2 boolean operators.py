leeftijd = int(input('Wat is je leeftijd?:'))
paspoort = input('Ben je in bezit van een Nederlands paspoort(J/N)')
if leeftijd >= 18 and paspoort == 'J':
    print('Mooi! Je bent ', leeftijd, ' jaar en in een bezit van een paspoort. Je mag stemmen!')
else:
    print('Helaas, je mag niet gaan stemmen')