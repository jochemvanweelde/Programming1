infile = open('kaartnummers.txt')
regels = infile.readlines()
hoeveelRegels = len(regels)
print("Deze file telt", hoeveelRegels, "regels")
list = []
for line in regels:
    line2 = line.split(',')
    list.append(int(line2[0]))
regel = list.index(max(list)) + 1
print('Het grootste kaartnummer is:', max(list), 'en staat op regel', regel)
