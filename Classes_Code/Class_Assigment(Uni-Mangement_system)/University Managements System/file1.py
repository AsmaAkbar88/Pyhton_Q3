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
# ------- Create Courses -------
c1 = Course(1001 , "Python")
c2 = Course(1002 , "English")

# ------- Create Department and Add Courses -------
d1 = Department("I.T")
d2 = Department("Science")
d1.add_course(c1.c_name)
d2.add_course(c2.c_name)


# ------- Create Students and Register to Courses -------
s1 = Student("Bushra", 22, "GIAIC1122")
s2 = Student("Atiqa", 23, "GIAIC1123")

s1.register_For_Cources(c1.c_name)
s2.register_For_Cources(c2.c_name)

c1.add_Student(s1.name)
c2.add_Student(s2.name)

# ------- Create Instructors and Assign to Courses -------
i1 = Instructor("Sir Hammad" , 30 , 50000)
i2 = Instructor("Sir Hamzah" , 30  , 60000)

c1.set_Instructor(i1.name )
c2.set_Instructor(i2.name)



# ------- Print Summary -------
print("Department1:", d1.__dict__)
print("Department2:", d2.__dict__)
print("Course 1:", c1.__dict__)
print("Course 2:", c2.__dict__)
print("Student 1:", s1.__dict__)
print("Student 2:", s2.__dict__)
