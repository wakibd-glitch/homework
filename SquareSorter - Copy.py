import math
evens = []
odds = []

def perfect_square(i):
    if i < 0:
        return False
    sqrtI = math.isqrt(i)

    return sqrtI * sqrtI == i



print("Give me ranges for sorting squares")
range1 = input("Range1: ")
range2 = input("Range2: ")

intrange1 = int(range1)
intrange2 = int(range2)

numList = []


for i in range(intrange1,intrange2+1):
    numList.append(i)




square_numbers = [num for num in numList if perfect_square(num)]




for a in square_numbers:
    if a % 2 == 0:
        evens.append(a)
    else:
        odds.append(a)

print("Here are your even and odd numbers: ")
print(evens)
print(odds)