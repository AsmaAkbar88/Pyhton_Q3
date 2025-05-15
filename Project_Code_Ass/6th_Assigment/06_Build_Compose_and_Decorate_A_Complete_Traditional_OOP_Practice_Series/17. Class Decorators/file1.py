def fun(cls):
    def grett(self):
        return "ye tu chala do"
        
    cls.grett = grett
    return cls
    
@fun
class Person():
    def __init__(self , name):
        self.name = name

retul = Person("mona")
print(retul.name)
print(retul.grett())

# Output: mona
# ye tu chala do