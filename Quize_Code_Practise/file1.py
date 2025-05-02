# x = 1000 
# y = 1000
# print(x is y)     # Output: True
# print(x == y)     # Output: True

# _____________________________________


# print(bool(""))  # Output: False

# ________________________________________


# print(isinstance(3.14, int))  # Output: False

# __________________________________________


# x = "Hello"
# print(x[::-1])                 # Output:  olleH

# ____________________________________________

# for i in range(3):
#     # print(i)                 # Output:  0 1 2


# _______________________________________________


# ye sari data type hy 
# a = dict()
# b = set()
# c = frozenset()
# d = tuple()
# e = complex()
# f = float()
# g = int()

# print(type(a) ,type(b) , type(c) ,type(d) , type(e) , type(f) , type(g))

# _______________________________________________________________________________
# Complex Type in Python 

# naame = 5 + 10j
# print(naame)            #Output: (5+10j)
# print(type(naame))      #Output: complex

# print(naame.real)       #Output:   5.0
# print(naame.imag)      #Output:   10.0

#   ________________________________________________________________________________


name2 = "Asma is a good girl"
num1 = "Asma124"


# print(name2.capitalize())   #Output: Asma is a good girl
# print(name2.count("s"))     #Output: 2
# print(name2.endswith("l"))  #Output: True
# print(name2.istitle())      #Output: False    pehla letter capital (sb ky shoro ky words wo check kry ga)
# print(name2.title())        #output:   Asma Is A Good Girl
# print(name2.islower())      # False   capital "A" ki wajah se
# print(name2.isalpha())        # False (Because is main space hyis liye true hy)
# print(name2.isalnum())        #Output: False   kyun ke alphabets hain (aur no space/symbol) +
# # True, kyunke a
# lphabets + numbers hain
# print(num1.isalnum())
# print(name2.upper())        #Output: ASMA IS A GOOD GIRL
# print(name2.lower())        #Output: asma is a good girl
# print(name2.isdigit())        # False
# print(name2.replace("A", "qi"))   # qisma  replace "A" with "qi"
# print(name2.find("m"))      #Output: 2  (Ye position dekhta hy)
# print(name2.index("m"))     #Output: 2  (ye bhi position dekhta hy)
# print(name2[ :: -1])        #Output: lrig doog a si amsA
# print(name2[ : 2])          #Output: As
# print(name2[ 2 :])          #Output: ma is a good girl
# print(name2.startswith("z"))#Output: False
# print(name2.isdigit())      #Output: Flase
# print(" ".join(name2))      #Output: A s m a   i s   a   g o o d   g i r l
# print(",".join(name2))     #Output: A,s,m,a, ,i,s, ,a, ,g,o,o,d, ,g,i,r,l
# print("___" * 20)

# _________________________________________________________________________________
#break method:________

# number = [1,2,3,4,5,6,7,8]

# for i in number:
#     if i == 7:
#         print("Number found 7")
#         break
# else:
#      print("Number not found")

# _____________________________________________________________________________________

#continue

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)       #output  0 ,1, 2, 4

# ___________________________________________________________________________________

#pass

# for i in range(5):
    # if i == 3:
    #     pass
    # print(i)       #output  0 ,1, 2, 3, 4


# ___________________________________________________________________________________
# For method
# # throwawy

# for _ in range(5):

#     print(f"Hello, world Iteration {_}")

# print("____" * 30)
# for _ in range(1 , 6):

#     print(f"Hello, world Iteration {_}")



# __________________________________________________________________________________

# list method

# fruits = ["Apple"  , "Banana"]
# fruits.append("Kiwi")   #Output:   ['Apple', 'Banana', 'Kiwi']



# a = fruits.count("Kiwi")                  #Output: 1
# print(f"1.      Ye \"count()\" bas count kr rha hy ye kitni bar aya hay:  {a}")


# # fruits.clear()                              #Output: []
# print(fruits)
# # _______________________________________________________________________________

# fruits.copy()
# print(f"2.      yahan \"copy\" kiye hen fruits: {fruits}")


# num  = [ 1, 7, 9]
# fruits.extend(num)
# print(f"3.      ye \"extend\" method hy:   {fruits}")
# # Output:  ['Apple', 'Banana', 'Kiwi', 1, 7, 9]  2 list ko aps main milta hy.


# aa = fruits.index("Kiwi")
# print(f"4.      ye \"index\" index btiye ga ky kon sy number py hay:  {aa}")                #Output: 4

# fruits.insert(2 , 777)
# print(f"5.      ye \"insert\" os ko osy number ki jhga rkh dy ga { fruits}")
 #Output:  ['Apple', 'Banana', 777, 'Kiwi']]

# --------------------------------------------------------------------



# fruits.pop()
# print(f"6.      ye \"pop\" ka method hy ye last sy delete kr day ga:  {fruits}")
#Output:     ['Apple', 'Banana']


# ac = fruits.pop()
# print(f"7.      ye \"pop\" ka method return ho rha hy: \"{ac}\" & {fruits}")

# -------------------------------------------------------------------------------------------------

# fruits.remove("Apple")
# print(f"8       ye \"remove\" hy ye dlete kr day ga:  {fruits}")
#Output: ['Banana', 777, 'Kiwi']

# fruits.reverse()
# print(f"9.      ye \"reverse\" mehod hy ye ulta chaly ga:  {fruits}")
# #Outout:     ['Kiwi', 'Banana', 'Apple'
# # __________________________________________________________________________________________


# num1 = [6 ,5,4 , 1, 4, 2, 3]
# num1.sort()
# print(f"1,      ye \"sort\" ye trteeb sy day ga {num1}")   #Output:   [1, 2, 3, 4, 4, 5, 6]


# num1.reverse()
# print(f"2.      ye \"reverse\" ye ulta aye ga:   {num1}")  #Output:   [6, 5, 4, 4, 3, 2, 1]


# num2 = [8,3 ,2, 1,4, 2,2 ,6 ,0]
# num2.sort(reverse=True)
# print(f"3.      ye \"reverse\" ye ulta aye ga:   {num2}")   #Output:   [8, 6, 4, 3, 2, 2, 2, 1, 0]

# _____________________________________________________________________________________________


# fruuits2 = ["Orange" , "Mango" , "Water"]
# print(" ".join(fruuits2))                    #Output:    Orange Mango Water

# print( " , ".join(fruuits2))                 #Output:     Orange , Mango , Water

# ______________________________________________________________________________________________


# fruits = [ "Apple" ,"Oranges", "Grapes" , "Kiwi"]
# # fruits.sort(key=len)
# # print(fruits)      #Output:   ['Kiwi', 'Apple', 'Grapes', 'Oranges']   choty sy braa==========>>

# fruits.sort()
# print(fruits)     #Output:      ['Apple', 'Grapes', 'Kiwi', 'Oranges']

                           
# _______________________________________________________________________________________________

# fruits = [ "Apple" , "Grapes" , "Kiwi","Oranges"]   #Ye sort alpebts sy kr rha hy 
# fruits.sort(key=lambda fruit: fruit[0])        #Output:  ['Apple', 'Grapes', 'Kiwi', 'Oranges']
#                                                 ye index ky[1] waly words ly rha hy.
# fruits.sort(key=lambda fruit: fruit[1])        #Output:  ['Kiwi', 'Apple', 'Grapes', 'Oranges']
# print(fruits)

# ___________________________________________________________________________________________________
#list
# student = ("Ali" , "Taimoor" , "Toheed " , "Zeeshan")
# Tple = student.count("Ali")                 #Output:    1
# print(Tple)                     


# print(student.index("Ali"))                #Output:  0


# ____________________________________________________________________________________________________

# a = ()
# print(type(a))             #       <class 'tuple'>
# print(a)

# b = {}
# print(type(b))             #       <class 'dict'>
# print(b)        


# c = dict()
# print(type(c))             #       <class 'dict'>
# print(c)       

# d = set()
# print(type(d))             #     cls   <class 'set'>
# print(d)      

# _______________________________________________________________________________________________

# a = dir(str)
# print(a)         #Output: is sy sari data type aae gi dic

# _____________________________________________________________________________________________
# match & case

# def check_status(Code):
#     match Code:
#         case (200):
#             print("Ok")
#         case (400):
#             print("Bad Request")
#         case (404):
#             print("Not Found")
#         case (500):
#             print("Internal Server Error")
#         case (200):
#             print("Unknow Status Code")
# check_status(200)
# ______________________________________________________________________________________________

student = {
    "name"  : "Sir Ameen",
     "Roll" :   9900
}
# 
# for score , student in student.items():    #Output:   name , Sir Ameen Roll , 9900
#    print(f" {score} , {student} ")

# student["name"] = "Sir Mubashir"        #Output:        {'name': 'Sir Mubashir', 'Roll': 9900}
# del student["name"]                     #Output:        {'Roll': 9900}
# student["slot"] = "Friday"              #Output:        {'Roll': 9900, 'slot': 'Friday'}
# # print(student.values())                 #Output:         dict_values([9900, 'Friday'])
# # print(student.keys())                   #Output:         dict_keys(['Roll', 'slot'])   
# print(student.items())                  #Output:         dict_items([('Roll', 9900), ('slot', 'Friday')])
# # print(student.get("slot"))                #Output:         Friday
# # student.update({"teacher" : "Sir Hamzah"})#Output:          'Roll': 9900, 'slot': 'Friday', 'teacher': 'Sir Hamzah'}
# # print("9900" in student.values())         #Output:          False
# for k , v  in student.items():
#     print(k , v)     #Output:     Roll 9900
# #                                 slot Friday
# print(student)


# ________________________________________________________________________________________________

# num = [3 ,5,6, 7,9,9, 4,2,3]
# print(3 in num)                #Output       True
# _________________________________________________________________________________________________
# a = 5
# b = 2 
# print( a % b)  #Output:  jo reh gya wo aye ga (1)


# _______________________________________________________________________________________________


# x = 10
# def outer():
#     x = 20
#     def inner():
#         nonlocal x
#         x = 30
#     inner()
#     print("Inner x: " , x )    #Output:        Inner x:  30
# outer()
# print("Global Outer x:"  , x)   #Output:       Global Outer x: 10

# _____________________________________________________________________________________
# def outer(x):
#     def inner(y):
#         return x +y
#     return inner

# add = outer(5)
# add2 = outer(10)

# print(add(3))
# print(add2(3))    #Output 8 : 13
# print("__" * 20)
# add_1 = outer(5)
# result = add_1(3)

# print(f"ye hmra hy single fun:            {result}")
# # __________________________________________________________________________________________


# my_list = [1 ,2,3]
# my_list.insert(0 , 0)
# print(my_list)                   #Output:   [0, 1, 2, 3]

# # ___________________________________________________________________________________________



# my_tuple = (1 ,2 ,3 )
# print(my_tuple * 2)               #Output:   (1, 2, 3, 1, 2, 3)

# # __________________________________________________________________________________________

# my_dict = { "a" : 1 , 
#             "b" : 2
#             }

# # my_dict["c"] = 8   #Output:  {'a': 1, 'b': 2, 'c': 8}
# my_dict.get("b" , 3)
# print(my_dict)                        #Output:   {'a': 1, 'b': 2}


# # _________________________________________________________________________________________

# my_tuple2 = (1 ,2 , 3)
# my_tuple2 += (4 ,5)
# print(f" ye tuple2:     {my_tuple2}")   #Output:    (1, 2, 3, 4, 5)

# # __________________________________________________________________________________________


# s1 = {1 ,2, 3}
# s2 = {3 ,4, 5}
# print(f" ye &:            {s1 & s2}")      #Output:   {3}

# # _________________________________________________________________________________________

# squ = [1, 2, 3, 4, 5]
# # squ = [x ** 2 for x in squ]        #Output:    [1, 4, 9, 16, 25]

# squ_number = [x ** 2 for x in squ if x % 2 == 0]     # output: [4, 16]
# print(squ_number)
# ____________________________________________________________________________________________

# t = ([1 ,2, 3] , "hello" )
# t[2].append(4)
# print(t)   #Output:    ([1, 2, 3, 4], 'hello')

# ____________________________________________________________________________________________

# my_dic = {"a" : 1 ,
#           "b" : 3
#           }

# my_dic["c"] = my_dic.get("c" , 3)
# print(my_dic)      #Output:       {'a': 1, 'b': 3, 'c': 3}




# _____________________________________________________________________________________________


# d = {}
# d[[1,2,3]]  = "value"
# print(d)             #Output:    error



# _____________________________________________________________________________________________

# def fun(x ,  ist = []):
#     ist.append(x)
#     return ist

# print(fun(3))   #Output:      [3]
# print(fun(2))    #Output:      [3, 2, ]
# print(fun(1))    #Output:      [3, 2, 1]

# _________________________________________________________________________________________

my_dic = {"a" : 1 ,
          "b" : 3 , 
          "g" : 6,
          "h"  : 4,
          }

# my_dic["c"] =  34     #output:    {'a': 1, 'b': 3, 'c': 34}
# del my_dic["c"]       #output:     {'a': 1, 'b': 3}
# print(my_dic.keys())  #Output:     dict_keys(['a', 'b', 'g', 'h'])
# print(my_dic.values())  #Output:     dict_values([1, 3, 6, 4])
# print(my_dic.items())   #Output:     dict_items([('a', 1), ('b', 3), ('g', 6), ('h', 4)])
# print(my_dic.get("a"))     #Ouutput:     1
# print(my_dic["a"])            #Output:     1
# my_dic.update({"d" : 87})     #Output:      {'a': 1, 'b': 3, 'g': 6, 'h': 4, 'd': 87}
# my_dic.pop("d")               #Output:       {'a': 1, 'b': 3, 'g': 6}
# my_dic.clear()                  #Output:        {}
# print(len(my_dic))                #Output:       4
# for b_key , c_value in my_dic.items():
#     print(b_key , c_value)
# # a 1
# # b 3
# # g 6
# # h 4

# print(my_dic)

# __________________________________________________________________________________

# name = "Abdullah"
# print(name[ 3 : -1])      #Output:   ulla

# __________________________________________________________________________________


# hello = "Hello world i am asma"
# print(hello.title())            #Output:  Hello World I Am Asma


# __________________________________________________________________________________

# name2 = "hello world subhan khalid"
# print(name2.replace("subhan khalid" , "Asma_Akbar"))    #Output:       hello world Asma_Akbar

# _________________________________________________________________________________



# name2 = "hello world subhan khalid"
# print(name2.find("a"))           #Output:  16
# print(name2.find("z"))           #Output:    -1



# _________________________________________________________________________________

# name2 = "Asma Akbar"
# print(name2.split())     #OUTPUT:           ['Asma', 'Akbar']
# print(name2.split(" "))     #OUTPUT:        ['Asma', 'Akbar']
# print(name2.split(","))     #OUTPUT:        ['Asma Akbar']

# _______________________________________________________________________________________

# numberr = [ 2 ,  5 ,  7,   2  , 4  , 6   , 8]
# a  = numberr.sort()
# print(a)       #output:  None

# numberr.sort()
# print(numberr)    #Output:        [2, 2, 4, 5, 6, 7, 8]



# numberr.sort(reverse=True)
# print(numberr)       #Output:     [8, 7, 6, 5, 4, 2, 2]

# ______________________________________________________________________________________
num = [ 4 , 6 ,65, 3, 21 , 54 , 32]
# num.reverse()
# print(num)        #Output:              [32, 54, 21, 3, 65, 6, 4]


# ______________________________________________________________________________________


# num2 = ["Apple" , "orange" , "Grapes" , "Banan"] 
# num2.reverse()
# print(num2)             #Output:        ['Banan', 'Grapes', 'orange', 'Apple']


# _______________________________________________________________________________

# x = 5
# x += 2

# print(x)       #Output:    7



# ___________________________________________________________________________________

# print(2 * 3 ** 2)      #Output:     18

# ___________________________________________________________________________________




# ____________________________________________________________________________________
# i = 0
# while True:
#     if i % 3 == 0:
#         break
#     print(i)
#     i += 1

# ________________________________________________________________________________

# dict2  = {
#     "name" : "Asma",
#     "roll" : 99,
#     "studen" : {"class" : "KG",
#                 "class2" : "One",
#                 "class3" : "Nursery"
#                 }
# }
# print(dict2["studen"]["class"])     #Output:   KG
# print(dict2["studen"]["class2"])    #Outout: One
# print(dict2["studen"]["class3"])    #Output:  Nursery
# __________________________________________________________________________



# mydict = {"name": "Mona", "age": 16}

# print(mydict.get("roll"))                #Output: None

# _____________________________________________________________________________


# set  = {9, 9.0}
# print(set)         #Output: 9

# set  = {str(9), 9.0}
# print(set)        #Output:   {9.0, '9'}

# _______________________________________________________________________________


# for i in range(10 , 0 , -1):
#     print(i )
#     utli counting aae gi
# _________________________________________________________________


# for num in range(-2 , -5 , -1):
#     print(num)
# #OUTPUT: 
# # -2
# # -3
# # -4

#________________________________________________________________________________


# multiply = lambda x, y: x * y
# result = multiply(5, 3)
# print(result)                              # Output: 15
# ________________________________________________________________________________

# my_dict  = "Asma Akbar"
# result = my_dict.split("a")
# print(result)            #Output:            ['Asm', ' Akb', 'r']

# # _____________________________________________________________________________________


# def fun (x , y = []):
#     y.append(x)
#     return y

# # print(fun(1))                         #output:     [1]
# print(fun(2 , [3, 4]))                #Output:   [3, 4, 2]
# print(fun(3))                          #OUTPUT:  [1, 3]

# ______________________________________________________________________________________

# def fun():
#     x = 10
#     return x
# print(x)               #OUTPUT: Error

# ______________________________________________________________________________________________
  

# print(2**3)

# _____________________________________________________________________________________

# my_str = " , "
# new_var = my_str.join("python")
# print(new_var)          #Output:         p , y , t , h , o , 
                
# ____________________________________________________________________________________

# a = "Hello"
# b = "Hello"
# print(a is b)               #Output: True


# num2 = [1, 4, 5]
# num1 = [1, 4, 5]
# print(num2 is num1)         #Output: false

# b  = 5
# c = 5

# print(b is c)       #OUTput:   True
# ___________________________________________________________________________________

# print(int(True))          #Output: 1
# print(int(False))         #Output: 2



# _____________________________________________________________________________________

# # x = 5
# while x:
#     print(x)
#     x -=                #Output:   5 4 3 2 1
    
# __________________________________________________________________________________________


# info = {"id" : 101 ,
#         "sar" : "name"}
# print(info.get("age", "notfound_your_age"))          #Output:        notfound_your_age


# ______________________________________________________________________________________________


# x = 0
# while x < 5:
#     if x == 3:
#      break
#     print(x)
#     x += 1
#      #output:  0 1 2

# ________________________________________________________________________________________________

# sum = 0
# for i in range(1 ,5):
#     sum += i
#     # print(i)
#     print(sum)


# __________________________________________________________________________________________

# t = (1, 2, 3)
# t[0] = 10

# print(t) #ERROR

# ______________________________________________________________________________________________


def fun(code):
    return [ x ** 2 for x in code if x % 2 == 0]
print(fun(range(6)))         #Output:      [0, 4, 16]


# _____________________________________________________________________________________________


