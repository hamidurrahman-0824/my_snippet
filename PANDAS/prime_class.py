import prime_check
class PrimeIter:
    def __init__(self,limit,start=0,step=1):
        self.start = start
        self.step = step
        self.limit = limit
        self.current = 0
    def __iter__(self):
        return self## the object itself is the iterator
    """def __iter__(self):
    return PrimeIteratorHelper(self.start, self.limit, self.step)
    """
    def __next__(self):
        self.current += self.step
        lmt = self.current+self.step
        if self.current<lmt:
            if prime_check.is_prime(self.current):
                return self.current
        else:
            raise StopIteration("Make start<limit")

obj = PrimeIter(2,20)
for i in obj:
    print(i)