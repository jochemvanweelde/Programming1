stations = ['Schagen','Heerhugowaard','Alkmaar','Castricum','Zaandam','Amsterdam Sloterdijk','Amsterdam Centraal','Amsterdam Amstel','Utrecht Centraal',"'s-Hertogenbosch",'Eindhoven','Weert','Roermond','Sittard','Maastricht']
def inlezen_beginstation(stations):
    while True:
        stationInput = input('Wat is je beginstation?:')
        for beginStation in stations:
            if beginStation == stationInput:
                return beginStation
            elif beginStation == 'Maastricht':
                print('De trein komt helemaal niet in', stationInput)
def inlezen_eindstations(stations, beginstation):
    beginStationIndex = stations.index(beginstation)
    while True:
        stationInput = input('Wat is je eindstation?:')
        for eindStation in stations:
            if eindStation == stationInput:
                if stations.index(eindStation) > beginStationIndex:
                    print('Ja hoor gelukt!')
                    return eindStation
                else:
                    print('De trein gaat hier niet heen!')

def omroepen_reis(stations, beginstation, eindstation):
    print("Het beginstation", beginstation, 'is het', stations.index(beginstation), 'e station in het traject.')
    print("Het eindstation", eindstation, 'is het', stations.index(eindstation), 'e station in het traject.')
    berekening = (stations.index(eindstation)-stations.index(beginstation))
    print('De afstand bedraagt', berekening, 'station(s).')
    print('De prijs van het kaartje is', berekening*5, 'euro.\n')
    print('Jij stapt in de trein in:', beginstation)
    for tussenstop in stations:
        if stations.index(tussenstop) > stations.index(beginstation) and stations.index(tussenstop) < stations.index(eindstation):
            print('-', tussenstop)
    print('Jij stapt uit in:', eindstation)

beginStation = inlezen_beginstation(stations)
eindStation = inlezen_eindstations(stations, beginStation)
omroepen_reis(stations, beginStation, eindStation)