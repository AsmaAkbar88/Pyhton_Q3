# ✅ 3. __mul__ → for * operator

class Multiplier:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return Multiplier(self.value * other.value)

    def __str__(self):
        return f"Value: {self.value}"

a = Multiplier(3)
b = Multiplier(4)
print(a * b)  # ✅ Output: Value: 12

