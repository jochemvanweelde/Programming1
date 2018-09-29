studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
listGemiddeldePS = []
def gemiddelde_per_student(studentencijfers):
    for list in studentencijfers:
        gemiddeldePS = (sum(list)/len(list))
        listGemiddeldePS.append(gemiddeldePS)
    return listGemiddeldePS
def gemiddelde_van_alle_studenten(studentencijfers):
    somListGemiddeldePS = sum(listGemiddeldePS)
    return (somListGemiddeldePS/len(studentencijfers))

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))