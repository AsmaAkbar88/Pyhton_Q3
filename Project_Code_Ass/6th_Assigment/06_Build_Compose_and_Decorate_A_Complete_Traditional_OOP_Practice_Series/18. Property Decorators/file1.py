class Product:
    def __init__(self, private):
        self._private = private

    @property
    def price(self):
        return self._private

    @price.setter
    def price(self, value):
        if value >= 0:
            self._private = value
        else:
            print("do not have balance")

    @price.deleter
    def price(self):
        print("delete message")
        del self._private



reult = Product(600)

print(reult.price)  

reult.price = 900  
print(reult.price) 

del reult.price   


#Ouput:  600
# 900
# delete message
# __________________________________________

