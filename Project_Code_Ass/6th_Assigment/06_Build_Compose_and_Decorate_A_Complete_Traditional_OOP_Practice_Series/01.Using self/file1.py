class Student:
    def __init__(self, name, marks):
        self.name = name      
        self.marks = marks  

    def display(self):
        print(f"My name is {self.name}")
        print(f"My marks out of 1000: {self.marks}")

student1 = Student("Asma Akbar", 900)
# print(student1.name , student1.marks)

student1.display()

# OUTPUT:  My name is Asma Akbar
# My marks out of 1000: 900

# _________________________________________________________________
