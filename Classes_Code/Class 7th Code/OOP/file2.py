class Teacher:
  def __init__(self , name:str , salary ="500 Dollar"):
    self.name =  name
    self.salary = salary


first_teacher = Teacher(name="Hamzah syed", salary="300")
print(first_teacher.name)