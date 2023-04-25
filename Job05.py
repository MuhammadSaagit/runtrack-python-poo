# import the Shape class from Job04.py
from Job04 import Shape
import math

# define the Rectangle class, which inherits from Shape


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# define the Circle class, which inherits from Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# create a rectangle instance and print its area
r = Rectangle(4, 5)
print("Rectangle area:", r.area())  # output: 20

# create a circle instance and print its area
c = Circle(3)
print("Circle area:", c.area())  # output: 28.274333882308138
