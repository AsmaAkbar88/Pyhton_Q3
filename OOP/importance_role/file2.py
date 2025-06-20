#✅ 2. __sub__ → for - operator


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(5, 7)
p2 = Point(2, 3)
print(p1 - p2)  # ✅ Output: Point(3, 4)
