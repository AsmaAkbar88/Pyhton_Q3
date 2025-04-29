from abc import ABC, abstractmethod

# ABSTRACTION: Abstract base class
class BankAccount(ABC):
    def __init__(self, name, balance):
        self._owner = name               # ENCAPSULATION: Protected attribute
        self.__balance = balance         # ENCAPSULATION: Private attribute

    def deposit(self, amount):
        self.__balance += amount         # Internal access to private balance

    def account_type(self):
        print("No specific type")

    # ABSTRACTION: Abstract method to be implemented by subclasses
    @abstractmethod
    def get_report(self):
        pass

    # Internal method to access private balance within child classes
    def _get_balance(self):
        return self.__balance

# INHERITANCE: BusinessAccount subclass
class BusinessAccount(BankAccount):
    def __init__(self, name, balance, company_name):
        super().__init__(name, balance)
        self.company_name = company_name

    def account_type(self):
        print("Business Account")

    # POLYMORPHISM: Different implementation of get_report()
    def get_report(self):
        return f"{self.company_name} balance is {self._get_balance()}"

# INHERITANCE: IndividualAccount subclass
class IndividualAccount(BankAccount):
    def __init__(self, name, balance, cnic):
        super().__init__(name, balance)
        self.cnic = cnic

    def account_type(self):
        print("Individual Account")

    # POLYMORPHISM: Different implementation of get_report()
    def get_report(self):
        return f"CNIC {self.cnic} balance is {self._get_balance()}"

# OBJECT CREATION
b1 = BusinessAccount("Hamzah", 1000, "Upwork")
b2 = BusinessAccount("Ali", 2000, "Not Upwork")
i1 = IndividualAccount("Sara", 1500, "35202-1234567-8")
#    ______________________________________________________________________________