class StringReverse:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

    def __str__(self):
        return self.reverse_words()



s = StringReverse(input("Enter String: "))
print(s)