
def greet():
  yield "Hello"
  yield "World"
# greet()                        #ans......generator object greet at 0x7b294f560460>
message = greet()

print( next(message) ) # Hello
# print( next(message) ) # World   ##aisy ye dono bar "hello" hi print dy rha hy is ky liye hmy is ko 1 varible main rkhna ho ga


# _______________________________________________________________________________
# message = greet()

# print(next(message))
# print(next(message))




