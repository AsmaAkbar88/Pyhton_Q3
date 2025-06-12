# MRO
class A:
    def show(self):
        print("A")

class B(A):
  pass

class C(A):
    pass
class D( C, B):
    pass

print(D.mro())
obj = D()
obj.show()

#OUTPUT:
# [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
# A