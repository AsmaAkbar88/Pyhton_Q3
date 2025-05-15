
class A:
    def show(self):
        print("Show from A")


class B(A):
    def show(self):
        print("Show from B")

class C(A):
    def show(self):
        print("Show from C")


class D(B, C):
    pass


obj = D()


obj.show()
# Output:   Show from B