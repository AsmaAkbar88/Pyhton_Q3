class Car:
    def __init__(self, brand):
        self.brand = brand  

    def start(self):      
        print(f"{self.brand} car is starting...")


car1 = Car("Toyota")
print(car1.brand)
car1.start()


#   output:       Toyota
# Toyota car is starting...
