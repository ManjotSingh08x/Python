import math

class Shape:
    pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def get_area(self):
        return math.pi * self.radius**2

    def get_perimeter(self):
        return math.pi * 2 * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def get_perimeter(self):
        return self.a + self.b + self.c

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Pentagon(Shape):
    def __init__(self, a):
        self.a = a

    def get_area(self):
        area = 5 * self.a**2 / (4 * math.tan(math.pi / 5))
        return area
    
    def get_perimeter(self):
        return 5 * self.a
    