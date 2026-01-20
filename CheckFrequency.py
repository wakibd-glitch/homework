testdic = {
    'Codingal': 3,
    'is': 2,
    'best': 2,
    'coding': 1
}

print(testdic)

freq = int(input("Which frequency value do you want to check: "))

count = list(testdic.values()).count(freq)

print("The value " , freq ," appears " , count , " times")
