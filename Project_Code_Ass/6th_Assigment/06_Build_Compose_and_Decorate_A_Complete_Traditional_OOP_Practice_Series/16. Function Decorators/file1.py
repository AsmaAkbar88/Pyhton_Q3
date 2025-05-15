def log_function_call(func):
    def wrapper():
        print("Function is being called")  
        return func()  
    return wrapper  


@log_function_call
def say_hello():
    print("Hello Mona! 😄")


say_hello()

# Output:  Function is being called
# Hello Mona! 😄