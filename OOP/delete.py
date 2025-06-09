class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"A {self.brand} {self.model} has been created.")

    def __del__(self):
        print(f"The {self.brand} {self.model} has been destroyed.")

    def display(self):
        print(f"Car: {self.brand} {self.model}")

my_car = Car("Toyota", "Corolla")
print(f"My car is a {my_car.brand} {my_car.model}.")
my_car.display()
del my_car


#output:
# A Toyota Corolla has been created.
# My car is a Toyota Corolla.
# Car: Toyota Corolla
# The Toyota Corolla has been destroyed.