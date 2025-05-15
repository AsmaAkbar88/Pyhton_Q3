class Person():
    def __init__(self, name):
        self.name = name

class Teacher(Person):                 #Inherit
    def __init__(self, name, subject):
        super().__init__(name) 
        self.subject = subject

teacher1 = Teacher("Asma", "Math")   #Inherit
print(teacher1.name , teacher1.subject)

person1 = Person("Zahid" ) 
print(person1.name)

# Ouptut:   Asma Math
# Zahid



