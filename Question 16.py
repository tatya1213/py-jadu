# Part 1: Creating the Animal class and defining its attributes
class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        return f"The {self.species} named {self.name} says {self.sound}"

# Creating objects (animals of different types)
dog = Animal("Buddy", "Dog", "Woof")
cat = Animal("Whiskers", "Cat", "Meow")

# Accessing attributes of the objects (instances)
print(dog.name)        # Accessing the 'name' attribute of the dog object
print(dog.species)     # Accessing the 'species' attribute of the dog object
print(dog.make_sound())  # Calling the make_sound method of the dog object

print(cat.name)        # Accessing the 'name' attribute of the cat object
print(cat.species)     # Accessing the 'species' attribute of the cat object
print(cat.make_sound())  # Calling the make_sound method of the cat object


# Part 2: Class Inheritance - Demonstrating single class inheritance

class Dog(Animal):  # Inheriting from the Animal class
    def __init__(self, name, breed, sound):
        super().__init__(name, "Dog", sound)  # Calling the parent class constructor
        self.breed = breed  # Adding an extra attribute specific to Dog class

    def display_breed(self):
        return f"The breed of {self.name} is {self.breed}"

# Creating an object of the Dog class (which inherits from Animal)
dog1 = Dog("Rex", "German Shepherd", "Bark")

# Accessing attributes and methods of the Dog class and inherited Animal class
print(dog1.name)          # Accessing the inherited 'name' attribute
print(dog1.species)       # Accessing the inherited 'species' attribute
print(dog1.sound)         # Accessing the inherited 'sound' attribute
print(dog1.make_sound())  # Calling the inherited make_sound method
print(dog1.breed)         # Accessing the 'breed' attribute of the Dog class
print(dog1.display_breed())  # Calling the display_breed method of the Dog class
