allItems = []
zeroCount = 0
temp = input('Δώστε έναν αριθμό ή "." για να σταματήσετε: ')
while (temp != '.') :
    intTemp = int(temp)
    if (intTemp == 0) :
        zeroCount += 1
    else :
        allItems.append(intTemp)
    temp = input('Δώστε τον επόμενο αριθμό ή "." για να σταματήσετε: ')
for x in range(zeroCount) :
    allItems.append(0)
print(allItems)
