class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self._balance = balance               # Protected attribute
        self.__pin = "1234"                   # Private attribute

    # Getter method for balance
    def get_balance(self):
        return self._balance

    # Setter method for balance
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
            print(f"Balance updated to {self._balance}.")
        else:
            print("Invalid amount. Balance cannot be negative.")

    # Getter method for pin (private attribute)
    def get_pin(self):
        return "Access denied. PIN is private."

    # Method to display account details
    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self._balance}")

# _____________________________________________________


account = BankAccount("Mona", 1000)
print(f"Account Holder: {account.account_holder}Balance (Direct Access): {account._balance}")   
# Output:    Account Holder: MonaBalance (Direct Access): 100

# print(account.__pin)  # ❌
print(account.get_pin())    #Access denied. PIN is private.

# ✔️ Getter method se balance dekhna
print(f"Initial Balance: {account.get_balance()}")    #Initial Balance: 1000

# ✔️ Setter method se balance update karna
account.set_balance(1500)    #OUTPUT:   Balance updated to 1500.

# ❌ Negative value dena
account.set_balance(-500)   #output:Invalid amount. Balance cannot be negative

# 🖥️ Display method se details dekhna
account.display()  #Account Holder: Mona  Balance: 1500
