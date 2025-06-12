# Decorators
def is_logged_in(fn):
  def wrapper():
    print("Checking login status...")
    print("✅ User is logged in")
    fn()
  return wrapper

@is_logged_in
def home_page():
  print("Rendering home page")

home_page()

#OUTPUT:
# Checking login status...
# ✅ User is logged in
# Rendering home page