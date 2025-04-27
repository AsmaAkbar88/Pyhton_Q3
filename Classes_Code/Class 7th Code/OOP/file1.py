class Student():
  def __init__(self, roll: str):
    self.name = "Osama"
    self.roll_number = roll


s1 = Student(roll="GIAIC123")
print(s1.roll_number)

s2 = Student( roll = "GIAIC321" )
print(s2.roll_number)
