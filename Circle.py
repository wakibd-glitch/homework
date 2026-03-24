import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Example usage
b = int(input("Radius: "))
c = Circle(b)

print("Radius:", c.radius)
print("Area:", c.area())
print("Perimeter:", c.perimeter())