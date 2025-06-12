class Student:
    quarter = 1  # class variable shared by all students

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @classmethod
    def next_quarter(cls):
        cls.quarter += 1
        print(f"✅ Advanced to Quarter {cls.quarter}")

    @staticmethod
    def school_greeting():
        print("👋 Welcome to ABC School! Let's learn and grow together.")


# Create students
s1 = Student("John", 20, "Male")
s2 = Student("Ali", 20, "Male")

Student.school_greeting()
Student.next_quarter()
Student.next_quarter()
Student.next_quarter()


print(s1.quarter)



# Access via class or instance
print(f"📚 Global Quarter (from class): {Student.quarter}")
print(f"📚 Quarter (from s1): {s1.quarter}")


# _________________________________________________________________
# OUTPUT
# 👋 Welcome to ABC School! Let's learn and grow together.
# ✅ Advanced to Quarter 2
# ✅ Advanced to Quarter 3
# ✅ Advanced to Quarter 4
# 4
# 📚 Global Quarter (from class): 4
# 📚 Quarter (from s1): 4
