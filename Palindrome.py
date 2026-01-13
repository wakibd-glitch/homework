# function
def palindrome(inputtuple):

    e = len(inputtuple)
    s = 0

    while s<e:
        if inputtuple[s] != inputtuple[e]:
            return False
        
        s = s + 1
        e = e -1
    return True



mytuple = (5,6,7,7,6,5)
if(palindrome(mytuple)):

    print("The tuple is flip flop")
else:
    print("Tuple is not Flip Flop")