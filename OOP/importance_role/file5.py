#✅ 5. __eq__ → for == comparison

class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

p1 = Person("Ali")
p2 = Person("Ali")
print(p1 == p2)  # ✅ Output: True
