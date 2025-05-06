class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee

    def show_details(self):
        return f"Department: {self.dept_name}, Employee: {self.employee.name}"


emp1 = Employee("Mona")


dept = Department("IT", emp1)


print(dept.show_details())
