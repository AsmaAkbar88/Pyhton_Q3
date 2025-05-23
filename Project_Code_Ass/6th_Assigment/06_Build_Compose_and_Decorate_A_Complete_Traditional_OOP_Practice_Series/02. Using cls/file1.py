class Counter:
    count = 0  

    def __init__(self):
        Counter.count += 1  

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

count1 = Counter()
count2 = Counter()
count3 = Counter()

Counter.show_count()

# ouput:   Total objects created: 3