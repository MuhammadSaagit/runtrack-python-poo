class Vehicle:
    def __init__(self, brand, year, price):
        self.brand = brand
        self.year = year
        self.price = price

    def informationVehicle(self):
        print(f"Make: {self.brand}\nYear: {self.year}\nPrice: {self.price}")


class Car(Vehicle):
    def __init__(self, brand, year, price):
        super(Car, self).__init__(brand, year, price)
        self.doors = 4

    def informationVehicle(self):
        super(Car, self).informationVehicle()
        print(f"Doors: {self.doors}")


car = Car("Toyota", 2021, 25000)
car.informationVehicle()
