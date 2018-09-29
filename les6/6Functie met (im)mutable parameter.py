lijst = ['a', 'b', 'c']
print(lijst)
def wijzig(lijst):
    del lijst[:]
    lijst.extend(['d', 'e', 'f'])
wijzig(lijst)
print(lijst)