class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
    
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

c = Countdown(5)

# for number in c:
    # print(number)
# Output

# 5
# 4
# 3
# 2
# 1
# 0

# --------------------------------------------------------------------
# seedhi counting

class Countdown:
    def __init__(self, end):
        self.start = 0
        self.end = end

    def __iter__(self):
    
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current

c = Countdown(5)

for number in c:
    print(number)
# Output

# 0
# 1
# 2
# 3
# 4
# 5
