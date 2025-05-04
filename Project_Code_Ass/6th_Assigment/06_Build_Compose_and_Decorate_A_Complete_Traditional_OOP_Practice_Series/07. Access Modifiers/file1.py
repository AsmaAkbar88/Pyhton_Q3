# class Employee():
#     def __init__(self , name , salary , ssn):
#         self.new_name = name         # Public variable
#         self._salary = salary        # Protected variable
#         self.__ssn = ssn             # Private variable


# account = Employee("Asma" , 3999 , "englis")
# print(f"Public Name: {account.new_name}")
# print(f"Protected Salary: {account._salary}")
# print(f"Private SSN : {account._Employee__ssn}")
# #  ________________________________________________________________________________________________

#step 02

class Employee():
    def __init__(self , name , salary , ssn):
        self.new_name = name         # Public variable
        self._salary = salary        # Protected variable
        self.__ssn = ssn             # Private variable

    def  get_salry(self):
        return self.__ssn


account1 = Employee("Asma Akbar" , 778999 , "Maths")
print(f"""my name is {account1.new_name}
      and 
      my salary is {account1._salary}
        and
          my favorite sunject is {account1.get_salry()}""")

# ____________________________________________________________________________________________________________________