class User():
  def __init__(self , email , password):
    self.email = email
    self.password = password


  def login(self):
    print("User Login")

  def logout(self):
    print("User Logout")

user = User("Noor@gmail.com"  ,  90090)
user.login()    #User Login
user.logout()    #User Logout


# _____________________


class Admin(User):
  def __init__(self , email , password):
    super().__init__(email , password)

  def login(self , admin_key):
    if not admin_key == "1234":
       print("Invalid Key")
    else:
       print("Admin Login")


admin1 = Admin("noor@gmail.com" , "2333")
admin1.login("555")                       #Outout:      Invalid Key

admin2  = Admin("noor@gmail.com" , "2333")
admin2.login("1234")                      #output:       Admin Login
