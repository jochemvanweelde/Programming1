try:
    totaalKosten= 4356
    aantal = int(input('Hoeveel mensen betalen?: '))
    kostenPerPersoon = totaalKosten / aantal
    print(kostenPerPersoon, 'euro per persoon')
except ZeroDivisionError:
    print('Delen door 0 is onmogelijk')
except TypeError:
    print('Je invoer moet een getal zijn, geen tekst!')
except ValueError:
    print('Je invoer moet hoger dan 0 zijn')