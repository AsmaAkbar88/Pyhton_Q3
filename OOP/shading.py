class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name          # Instance attribute
        self.age = age            # Instance attribute

dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)

Dog.species = "Canis lupus"        # Modify class attribute
dog1.species = "Canis aureus"      # Shadowing - new instance attribute
