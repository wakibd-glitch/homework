n = int(input("Give me a number: "))
odd_numbers = [x for x in range(n) if x % 2 != 0]
print(odd_numbers)

Fruits = ["apple","banana","pear","grape"]
print(Fruits)
CapitalFruits = [word.title() for word in Fruits]
print(CapitalFruits)