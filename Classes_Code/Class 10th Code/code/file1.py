from abc import ABC, abstractmethod

class Auth(ABC):
  @abstractmethod
  def login(self):
    pass

  def logout(self):
    print("Logout")

class LoginPassword(Auth):
  def login(self, email, password):
    print("Login Successfully")

class GoogleAuth(Auth):
  def login(self):
    print("Google Auth link")

class FacebookAuth(Auth):
  def welcome():
    print("Welcome")

user2 = FacebookAuth()

# ============================================================================================

user1= GoogleAuth()
user1.login()

user = GoogleAuth()
user.logout()
