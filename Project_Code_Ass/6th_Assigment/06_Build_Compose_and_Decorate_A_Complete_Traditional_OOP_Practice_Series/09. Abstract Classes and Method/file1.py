from abc import ABC , abstractmethod

class Shape(ABC):         # Abstract Base Class is ka mtb hy 
    @abstractmethod       #ye bas rule bane gi is ka child fun kry ga
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self , length , weight):
        self.length = length
        self.weight = weight



    def area(self):
        return self.length * self.weight


result = Rectangle(7 , 3)
print(result.area()) #OUput:   21