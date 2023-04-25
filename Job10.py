class Car:
    def __init__(self, brand, model, year, mileage):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__en_marche = False
        self.__reservoir = 50

    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_year(self, year):
        self.__year = year

    def get_year(self):
        return self.__year

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def get_mileage(self):
        return self.__mileage

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    def start(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("Car is started.")
        else:
            print("Error: Not enough fuel to start the car.")

    def stop(self):
        self.__en_marche = False
        print("Car is stopped.")

    def __verifier_plein(self):
        if self.__reservoir >= 5:
            return True
        else:
            return False


# example
car1 = Car("Mercedes-Benz", "C-Class", 2018, 5000)
print(car1.get_brand())  # Output: Mercedes-Benz
print(car1.get_model())  # Output: C-Class
print(car1.get_year())  # Output: 2018
print(car1.get_mileage())  # Output: 5000

car1.start()  # Output: Car is started.
car1.stop()  # Output: Car is stopped.

car1.set_brand("BMW")
print(car1.get_brand())  # Output: BMW
