class Calculator:
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def add_numbers(self):
        return self.number1 + self.number2

    def subtract_numbers(self):
        return self.number1 - self.number2

    def print_numbers(self):
        print("Number 1:", self.number1)
        print("Number 2:", self.number2)


calc = Calculator(9, 10)
print("The sum of the numbers is:", calc.add_numbers())
print("The difference of the numbers is:", calc.subtract_numbers())
calc.print_numbers()
