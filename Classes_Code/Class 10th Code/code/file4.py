# Callable
class Greeter:
    def __init__(self):
        self.name = "hamzah"
    def __call__(self):
        print("👋 Hello, I’m a callable object!")

g = Greeter()
g()  # ✅ callable — this works because of __call__()

#OUTPUT:
# 👋 Hello, I’m a callable object!
