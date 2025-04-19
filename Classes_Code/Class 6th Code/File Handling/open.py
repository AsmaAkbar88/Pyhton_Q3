# Step 1: File Write Mode "w"

file = open("new_file.txt" , "w")
file.write("1.Somthing add new line in first time")
file.write("\n \n2.Added 2nd Line")
file.write("\n \n 3.Added 3rd line")
file.close()

# with open("new_file.txt" , "w") as khas:
#  khas.write("Added new line with oepn file.txt")


#Step 2: File Read All 

# file = open("new_file.txt" , "r")
# content = file.read()
# print(content)
# file.close()


# Step 3: Read Lines (List form)
# kuch = open("new_file.txt" , "r")
# lines = kuch.readlines()
# print(lines)
# kuch.close()


# Step 4: With Statement for Reading (Safe method)
with open ("new_file.txt" , "r") as file:
 lines = file.readlines()
#  print(lines)




# Step 5: Read + Write Mode "r+"
 with open("new_file.txt" , "r+") as file:
  
  file.write("Aded 4th line\n")
  file.seek(0)
  veribale = file.read()
  print(veribale)


#   with open("new_file.txt", "a") as file:
#     file.write("\n4. Appended new line at the end")



# Agar tum last line mein likhna chahti ho to "a" (append mode) use karo:
with open("new_file.txt", "a") as file:
    file.write("\n4. Appended new line at the end")
    file.seek(0)
