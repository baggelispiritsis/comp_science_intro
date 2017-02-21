import math
numbers = list(map(int, input('Δώσε τουλάχιστον 5 αριθμούς χωρισμένους με κενό:\n').split()))
if (len(numbers) < 5) :
    print('Δεν δώσατε αρκετούς αριθμούς.')
    quit()
numbers.sort()
numbers.pop()
numbers.pop()
del numbers[0]
del numbers[0]
n = len(numbers)
average = sum(numbers) / n
total = 0
for x in numbers :
    total += (x - average)**2
total /= n
result = math.sqrt(total)
print('Αποτέλεσμα: ')
print(result)
