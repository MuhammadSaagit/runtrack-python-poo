class Person:
    def __init__(self, age=14):
        self.age = age

    def displayAge(self):
        print("Age:", self.age)

    def hello(self):
        print("Hello")

    def modifyAge(self, newAge):
        self.age = newAge


class Student(Person):
    def __init__(self):
        super().__init__()

    def goToCourse(self):
        print("I go to class")

    def displayAge(self):
        print("I am", self.age, "years old")


class Teacher(Person):
    def __init__(self, subjectTaught):
        super().__init__()
        self.__subjectTaught = subjectTaught

    def teach(self):
        print("start")


student = Student()
student.displayAge()  # Display the default age of the student
