class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof Woof!")  


result = Dog("Cutie_Cat", "Beagle")

print(result.name, result.breed)

result.bark()

# output:  Cutie_Cat Beagle
# Cutie_Cat says: Woof Woof!