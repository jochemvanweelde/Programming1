def kaartnummersTXT():
    infile = open('Kaartnummers.txt')
    text = infile.readlines()
    for line in text:
        line2 = line.split(',')
        enter = line2[1].rstrip('\n')
        print(enter, 'heeft kaarnummer:', line2[0])
kaartnummersTXT()