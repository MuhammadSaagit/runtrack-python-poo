class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def perimeter(self):
        return 2*(self.__length + self.__width)

    def area(self):
        return self.__length * self.__width


class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.__height = height

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def volume(self):
        return self.get_length()*self.get_width()*self.__height


# testing Rectangle
r = Rectangle(5, 4)
print("Rectangle perimeter:", r.perimeter())
print("Rectangle area:", r.area())
r.set_length(6)
print("New rectangle perimeter:", r.perimeter())
print("New rectangle area:", r.area())

# testing Parallelepiped
p = Parallelepiped(3, 4, 5)
print("Parallelepiped perimeter:", p.perimeter())
print("Parallelepiped area:", p.area())
print("Parallelepiped volume:", p.volume())
