list = [2,4,5,6,7,8,9,10,15,47,48,69,62,70,98]
minList = min(list)
maxList = max(list)+1 #anders pakt hij het laatste getal niet mee
for i in range(minList, maxList, 2):
    if i in list:
        print(i)