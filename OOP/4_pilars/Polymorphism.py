class Bird:
    def sound(self):
        print("Tweet tweet")

class Cat:
    def sound(self):
        print("Meow meow")

def animal_sound(animal):
    animal.sound()

# ✅ Use
b = Bird()
c = Cat()

animal_sound(b)  # Tweet tweet
animal_sound(c)  # Meow meow
