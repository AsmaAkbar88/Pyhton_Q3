class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("You must be at least 18 years old")
    else:
        return "You are allowed ✅"

try:
    user_input = int(input("Enter your age: "))
    print(check_age(user_input))
except InvalidAgeError as e:
    print("Error:", e)



# Output:  Enter your age: 4
# Error: You must be at least 18 years old
 
# Output:    Enter your age: 33
# You are allowed ✅