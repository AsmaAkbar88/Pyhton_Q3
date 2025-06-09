# ✅ 4. __str__ → for print() or str() output

class Car:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f"Car Model: {self.model}"

c = Car("Civic")
print(c)  # ✅ Output: Car Model: Civic
