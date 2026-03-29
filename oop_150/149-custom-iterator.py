class Count:
    def __init__(self,limit):
        self.limit = limit
        self.current = 0
    def __iter__(self):
        print("in iter block")
        print(self)
        return self
    # def __iter__(self):
    #     return self
    def __next__(self):
        print("in next block")
        if self.current<self.limit:
            self.current += 1
            return self.current
        raise StopIteration


# for x in Count(5):
#     print(x)
# exit()
class EvenNumbers:
    
    def __init__(self, limit):
        self.limit = limit
        self.num = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.num += 2
        
        if self.num <= self.limit:
            return self.num
        
        raise StopIteration
class Counter:
    def __init__(self,start):
        self.start = start
        
    def __iter__(self):
        print('Only once this block is used, it makes thing iterable.rest is handled by __next__')
        return self
    def __next__(self):
        if self.start<=0:
            raise StopIteration
        self.start-=1
        return self.start

obj = iter(Counter(5))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))