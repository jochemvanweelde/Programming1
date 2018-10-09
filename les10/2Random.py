import random
dubbel = 0
def monopolyworp():
    while True:
        dobbelsteen1 = random.randrange(1, 7)
        dobbelsteen2 = random.randrange(1, 7)
        totaal = dobbelsteen1 + dobbelsteen2
        if dobbelsteen1 == dobbelsteen2:
            dubbel += 1
            if dubbel == 3:
                print(dobbelsteen1, '+', dobbelsteen2, '=', totaal)
                print("HUP NAAR DE GEVANGENIS")
                break
            else:
                print(dobbelsteen1, '+', dobbelsteen2, '=', totaal)
        else:
            print(dobbelsteen1, '+', dobbelsteen2, '=', totaal)
            dubbel = 0
monopolyworp()