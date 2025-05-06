class Multiplier():
    def __init__(self , factor):
        self.factor = factor

    def __call__(self, number):
        return self.factor * number

    
obj = Multiplier(5)
result = obj(45)
print(result)