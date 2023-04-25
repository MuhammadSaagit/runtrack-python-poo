class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# create a rectangle instance and print its area
r = Rectangle(4, 5)
print(r.area())  # output: 20
