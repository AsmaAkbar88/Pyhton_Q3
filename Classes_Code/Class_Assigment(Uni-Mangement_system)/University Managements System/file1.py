#   ____________Person Class:

class Person():
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"My name is {self.name} and my age is {self.age}")




#   ____________Student Class:

class Student(Person):
    def __init__(self, name, age ,roll_numer ):
        super().__init__(name, age)
        self.roll_number = roll_numer
        self.courses = []

    def register_For_Cources(self , course):
        self.courses.append(course)



c_student = Student("iqra" , "20year" , 90)
c_student.register_For_Cources("Pyhton")
print( c_student.name , c_student.age , c_student.courses)


#   ____________Instructor Class:



class Instructor(Person):
    def __init__(self, name, age , salry):
        super().__init__(name, age)
        self.salry = salry
        self.courses = []

    def assignCourse(self , course) :
        self.courses.append(course)

        # ======================

#   ____________Course Class:

class Course():
    def __init__(self , c_id , c_name):
        self.c_id = c_id
        self.c_name = c_name
        self.student = []
        self.instructor = []

    def add_Student(self ,students):
        self.student.append(students)

    def set_Instructor(self , inst):
        self.instructor.append(inst)

#   ____________Department Class:
class Department():
    def __init__(self , d_name ):
        self.d_name = d_name
        self.d_course = []

    def add_course (self  ,d_course):
        self.d_course.append(d_course)
        


# ==================================================================================Object:

c_person = Person("iqra" , 20)
c_person.get_details()

print(f"Course1 : ")

Course 1: {'id': 101, 'name': 'Python', 'students': ['Sadaf'], 'instructors': ['Ali']} 