# Part 1
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)

print(car1.brand, car1.model, car1.year)
print(car2.brand, car2.model, car2.year)

# Part 2
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Bike(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type

bike1 = Bike("Yamaha", "Sport")
print(bike1.brand, bike1.type)
