def is_armstrong(n:int)-> bool:
	#n=134
	s = 0
	r = str(n)
	for digit in r:
		s+=int(digit)**len(r)
	return s==n
print(is_armstrong(123))
i = 0
"""
while i<1500:
	if is_armstrong(i):
		print(i)
	i+=1"""
from factorial import rcr_fact
def strong_num(n):
	digits = str(n)
	s=0
	for digit in digits:
		s += rcr_fact(int(digit))
	return s==n
print(strong_num(145))
for i in range(200):
	if strong_num(i):
		print(i)
def perfect_num(n):
	nums = []
	for i in range(1,n//2+1):
		if n%i==0:
			nums.append(i)
	r = sum(nums)
	return r == n
for i in range(1,2000):
	if perfect_num(i):
		print(i)
def power_by_loop(x,y):
	s = 0
	for _ in range(y):
		s = x*x
	return s
print(power_by_loop(5,2))
