class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name

class Father:
    def __init__(self, father_name):
        self.father_name = father_name

class Child(Mother, Father):
    def __init__(self, mother_name, father_name, child_name):
        Mother.__init__(self, mother_name)
        Father.__init__(self, father_name)
        self.child_name = child_name

    def show_family(self):
        print(f"Mother: {self.mother_name}, Father: {self.father_name}, Child: {self.child_name}")


family = Child("AMi" , "ABU" , "Mona")
print(f"AMI_NAME: {family.mother_name}, FATHER_NAME: {family.father_name} , Child_Name: {family.child_name}")

#output:  AMI_NAME: AMi, FATHER_NAME: ABU , Child_Name: Mona

family.show_family()  #output:     Mother: AMi, Father: ABU, Child: Mona