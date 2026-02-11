class IOString():
    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("Enter String: ")

    def print_string(self):
        print("Result is : ", self.str1.upper())

mystring = IOString()

mystring.get_string()
mystring.print_string()