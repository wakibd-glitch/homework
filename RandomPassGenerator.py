import random
import string

WhileRand = random.randrange(4,10)

Pass = []
counter1 = 0
counter2 = 0

while counter1 < WhileRand:
    RandVar = random.randrange(0,10)
    Pass.append(RandVar)
    counter1 = counter1 + 1


while counter2 < WhileRand:
    RandomChar = random.choice(string.ascii_letters)
    Pass.append(RandomChar)
    counter2 = counter2 + 1


random.shuffle(Pass)

PassString = [str(element) for element in Pass]

VarPass = "".join(PassString)

print("Here is your Password: ",VarPass) 

