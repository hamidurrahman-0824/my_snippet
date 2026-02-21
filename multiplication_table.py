def mul_table(n:int,times)-> str:
	if times ==0 or n ==0:
		return print('0')
	for i in range(1,times+1):
		print(f"{n} x {i} = {n*i}")
mul_table(0,10)
