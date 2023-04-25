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


rectangle = Rectangle(10, 5)

print("Rectangle length:", rectangle.get_length())
print("Rectangle width:", rectangle.get_width())

rectangle.set_length(15)
rectangle.set_width(7)

print("New rectangle length:", rectangle.get_length())
print("New rectangle width:", rectangle.get_width())
