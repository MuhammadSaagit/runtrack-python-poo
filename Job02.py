class Person:
    def __init__(self, age):
        self.age = age

    def displayAge(self):
        print("I am", self.age, "years old.")


class Student(Person):
    def __init__(self, age):
        super().__init__(age)

    def displayAge(self):
        print("I am a student and I am", self.age, "years old.")

    def hello(self):
        print("Hello!")

    def goToCourse(self):
        print("I'm going to class.")


class Teacher(Person):
    def __init__(self, age):
        super().__init__(age)

    def teach(self):
        print("Please and thank you. Let's get started with the lesson.")


# Creating a student object
student = Student(15)
student.displayAge()  # should print "I am a student and I am 15 years old."
student.hello()  # should print "Hello!"
student.goToCourse()  # should print "I'm going to class.\"\n\n# Creating a teacher object
teacher = Teacher(40)
teacher.displayAge()  # should print "I am 40 years old."
teacher.teach()  # should print "Please and thank you. Let's get started with the lesson."
