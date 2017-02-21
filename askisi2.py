a=input('Δώστε μια ακολουθία παρενθέσεων: ')
counter=0
flag=True
par=list(a)
for p in par :
    if (p == '('):
        counter+=1
    elif (p == ')'):
        counter-=1
        if (counter < 0):
            flag=False
if (counter != 0):
    flag=False
print(flag)
