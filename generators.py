#no while loop no range function how to calculate 1-10?
class Iter:
	def __init__(self,n):
		self.n = n
	def __iter__(self):
		self.current = -1
		return self
	def __next__(self):
		self.current+=1
		if self.current>=self.n:
			raise StopIteration
		return self.current
x = Iter(5)

def gen(n):
	for i in range(n):
		yield i
for i in gen(4):
	print(i)

class CountDown:
	def __init__(self,start):
		self.current = start
	def __iter__(self):
		return self
	def __next__(self):
		if self.current <= 0 :
			raise StopIteration
		value = self.current
		self.current -= 1
		return value
for num in CountDown(5):
	pass
class Even:
	def __init__(self,start,limit):
		self.current = start
		self.limit = limit
	def __iter__(self):
		return self
	def __next__(self):
		if self.limit<=self.current:
			raise StopIteration
		else:
			self.current+=2
			return self.current if self.current<=self.limit else self.current-2
			
obj1 = Even(22,29)

for i in obj1:
	print(i)
