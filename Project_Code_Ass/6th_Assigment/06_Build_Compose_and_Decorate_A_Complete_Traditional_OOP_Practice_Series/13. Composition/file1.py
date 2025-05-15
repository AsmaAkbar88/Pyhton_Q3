class Engine:
    def start(self):  
        return "Engine start"

class Car:
    def __init__(self, engine):
        self.engine = engine

    def strt(self):
        return self.engine.start() 

engis = Engine()
car = Car(engis)
print(car.strt())
 #OUput: Engine start