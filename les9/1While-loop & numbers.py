somList=[]
getal = 1
while getal != 0:
    getal = int(input("Geef een getal:"))
    somList.append(getal)
print("er zijn", (len(somList) - 1), "getallen ingevoerd, de som is:", sum(somList))