stations = ['Schagen','Heerhugowaard','Alkmaar','Castricum','Zaandam','Amsterdam Sloterdijk','Amsterdam Centraal','Amsterdam Amstel','Utrecht Centraal',"'s-Hertogenbosch",'Eindhoven','Weert','Roermond','Sittard','Maastricht']
def inlezen_beginstation(stations):
    while True:
        stationInput = input('Wat is je beginstation?:')
        for station in stations:
            if station == stationInput:
                return station
def inlezen_eindstations(stations, beginstation):
    print('')