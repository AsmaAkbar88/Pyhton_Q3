import time

def character (text : str):
  for x in text:
    yield x
    
# step 01

message = character("Hello world")

# print(next(message))       #ans....h
# print(next(message))       #ans....e
# print(next(message))       #ans....l
# print(next(message))       #ans....l
# print(next(message))       #ans....o

# ______________________________________________________

# step 02
for y in message:
  print(y , end = "" ,flush= True )
  time.sleep(0.04)

# _________________________________________________________________________________________step 02
#ye sir hamza ka code hy 

import time

# Generator that yields one character at a time
def chatbot_typing_simulator(text: str):
    for char in text:
        yield char


# Function that consumes the generator with a delay (simulates typing)

for char in chatbot_typing_simulator("\nHello World...."):
  print(char, end='', flush=True)
  time.sleep(0.04)  # Delay to simulate typing



