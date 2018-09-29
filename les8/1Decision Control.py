def seizoen(maand):
    if maand >= 3 and maand <= 5: #3=Maart tot en met 5=mei -> Lente
        print("Lente")
    elif maand >= 6 and maand <= 8: #6=juni tot en met 8=augustus -> Zomer
        print("Zomer")
    elif maand >= 9 and maand <= 11: #9=september tot en met 11=november -> Herfst
        print("Herfst")
    elif maand >= 1 and maand <= 12: #1= Januari tot en met 12= december dit geld ook voor maart maar omdat het boven al genoemd is word er geen winter geprint. (Jan, feb, dec [1,2,12])
        print("Winter")
    else:
        print("Deze maand bestaat niet") #lager dan 1 of hoger dan 12 resulteert in deze print
maandnummer = int(input("Geef het nummer van de maand op:"))
seizoen(maandnummer)