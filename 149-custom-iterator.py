class Count:
    def __init__(self,limit):
        self.limit = limit
        self.current = 0
    # def __iter__(self):
    #     print("in iter block")
    #     print(self)
    #     return self
    def __next__(self):
        print("in next block")
        if self.current<self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration
# x = Count(10)
for x in Count(5):
    print(x)
