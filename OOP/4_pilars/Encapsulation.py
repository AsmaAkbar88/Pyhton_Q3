class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # private data

    def show_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

# ✅ Use
account = BankAccount("MONA", 1000)
print("Balance:", account.show_balance())  # 1000

account.deposit(500)
print("New Balance:", account.show_balance())  # 1500
