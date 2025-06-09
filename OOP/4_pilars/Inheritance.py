class Animal:
    def eat(self):
        print("I can eat.")

class Dog(Animal):  # Inheriting Animal
    def bark(self):
        print("I can bark.")

# ✅ Use
dog = Dog()
dog.eat()   # inherited from Animal  (I can eat.)
dog.bark()  # apna method     (I can bark)
