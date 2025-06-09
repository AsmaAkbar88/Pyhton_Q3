class Bird:
    def fly(self):
        return "Flying high!"

class Fish:
    def swim(self):
        return "Swimming deep!"

class FlyingFish(Bird, Fish):  # Child of both
    pass

flying_fish = FlyingFish()
print(flying_fish.fly())   #output:   Flying high
print(flying_fish.swim())   #Ouptut:    Swimming deep!
# 
