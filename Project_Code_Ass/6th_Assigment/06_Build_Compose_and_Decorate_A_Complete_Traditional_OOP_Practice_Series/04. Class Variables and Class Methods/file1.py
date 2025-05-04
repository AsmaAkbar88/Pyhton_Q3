class Bank:
    
    bank_name = "HBL Bank"

    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

acc1 = Bank("Asma")
acc2 = Bank("Zoahib")

print(f"{acc1.customer_name} belongs to {acc1.bank_name}")
print(f"{acc2.customer_name} belongs to {acc2.bank_name}")


print("___"*20)


Bank.change_bank_name("UBL Bank")


print(f"{acc1.customer_name} now belongs to NEW {acc1.bank_name}")
print(f"{acc2.customer_name} now belongs to NEW  {acc2.bank_name}")
