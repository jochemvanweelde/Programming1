def kwadraten_som(grondgetallen):

    list=[]

    for i in grondgetallen:
        if i >= 0:
            getal = i ** 2
            list.append(getal)
    return(sum(list))


print(kwadraten_som([4, 5, 3, -81]))
#50