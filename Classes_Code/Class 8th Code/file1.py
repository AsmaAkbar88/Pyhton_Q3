# simple

# class BankAccount():
#     def __init__(self):
#        self.name  = "hamzah"
#        self.balance  = 1000


# account1 =  BankAccount()
# print(f"This is {account1.name} account & his balance is {account1.balance}")


# ______________________________________________________________________________________________

# class BankAccount():
#     def __init__(self, name ,  balance):
#        self.name  = name
#        self.balance  = balance


# account1 =  BankAccount(name = "Asma" ,  balance =  1000)
# print(f"This is {account1.name} account & his balance is {account1.balance}")

# account2 =  BankAccount(name = "Bisma" ,  balance =  1000)
# print(f"This is {account2.name} account & his balance is {account2.balance}")

# __________________________________________________________________________________________

# class BankAccount():
#     def __init__(self, name ):
#        self.name  = name
#        self.balance  = 1000

 
#     def depostie(self , amount_balanc
#         self.balance += amount_balance

# account1 =  BankAccount(name = "Ali" )
# account1.depostie(4000)
# print(f"This is {account1.name} account & his e):balance is {account1.balance}")



# ____________________________________________________________________________________________________

#private balance ko access krna:_________



# class BankAccount():
#     def __init__(self, name ):
#        self.name  = name
#        self.__balance  = 1000

#     def get_balance(self):
#         return self.__balance

# account1 = BankAccount("ALI")

# print(f"my name is {account1.name}  and my balance is {account1.get_balance()}")

# ________________________________________________________________________________________________

#inheritance:~



# class BankAccount():
#     def __init__(self, name ):
#        self.name  = name
#        self.__balance  = 1000


# class BusinessAccount(BankAccount):
#     def __init__(self , company , name):
#         super().__init__(name)
#         self.owner_company = company


# account1 =  BusinessAccount("Upword" , "Ali")
# account2 =  BusinessAccount("A.J" , "Noor")

# print(f"My new company name is \"{account1.owner_company}\" and my name is \"{account1.name}\"")
# print(f"My new company name is \"{account2.owner_company}\" and my name is \"{account2.name}\"")


# _________________________________________________________________________________________________

#protucted class



# class BankAccount():
#     def __init__(self, name,  ):
#        self.name  = name
#        self._balance  = 1000

# class BusinessAccount(BankAccount):
#     def __init__(self , company , name):
#         super().__init__(name)
#         self.owner_company = company




# account1 = BusinessAccount("uperwork" , "zeeshan")
# print(f"My name is \"{account1.name}\" and my comapny name is \"{account1.owner_company}\" & my balance is \"{account1._balance}\""  )


# _______________________________________________________________________________________________