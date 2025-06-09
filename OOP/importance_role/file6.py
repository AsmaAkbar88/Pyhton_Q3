#✅ 6. __len__ → for len() function

class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

ml = MyList([1, 2, 3, 4])
print(len(ml))  # ✅ Output: 4
