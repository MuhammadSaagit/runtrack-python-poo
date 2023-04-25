class Animal:
    def __init__(self, name, species):
        self.name = name
        self.age = 0
        self.species = species

    def get_older(self):
        self.age += 1
        print(self.name, "is now", self.age, "years old.")

    def set_species(self, new_species):
        self.species = new_species

    def set_name(self, new_name):
        self.name = new_name


# Creating an instance of the Animal class
animal_1 = Animal("Leo", "Lion")

# Printing the name, age, and species of the animal object
print("Name:", animal_1.name)
print("Age:", animal_1.age)
print("Species:", animal_1.species)

# Changing the species of the animal object using the "set_species" method
animal_1.set_species("Tiger")
print("New Species:", animal_1.species)

# Changing the name of the animal object using the "set_name" method
animal_1.set_name("Simba")
print("New Name:", animal_1.name)

# Making the animal object older using the "get_older" method
animal_1.get_older()
