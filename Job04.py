class Person:
    def __init__(self, name, first_name):
        self.name = name
        self.first_name = first_name

    def sepresenter(self):
        return f"My name is {self.name} {self.first_name}"


person1 = Person("Robberto", "Saagito")
print(person1.sepresenter())  # Output: My name is X X
