def sieve_of_dhon(n:int)-> list[int]:
	dhon = [True]*n
	dhon[0]=dhon[1]= False
	for i in range(2,int(n**0.5)+1):
		for j in range(i**2,n,i):
			dhon[j] = False
	for k in range(2,len(dhon)):
		if dhon[k]:
			print(k)
		
sieve_of_dhon(55)
