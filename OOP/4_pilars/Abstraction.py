class CoffeeMachine:
    def make_coffee(self):
        self.__boil_water()
        self.__add_coffee()
        print("☕ Coffee ready!")

    def __boil_water(self):
        print("Boiling water...")

    def __add_coffee(self):
        print("Adding coffee...")

# ✅ Use
machine = CoffeeMachine()
machine.make_coffee()


# #output:   Boiling water...
# Adding coffee...
# ☕ Coffee ready!