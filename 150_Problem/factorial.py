def factorial(n:int)-> int:
	if n<0:
		return n
	if n==0:
		return 1
	m = 1
	for i in range(1,n+1):
		m*=i
		
	return m


def rcr_fact(n:int)->int:
	if n==0:
		return 1
	return n*rcr_fact(n-1)
