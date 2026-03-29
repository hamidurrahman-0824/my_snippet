lst = [0,1,0.4,True,False,'a',2]
s = 0
for item in lst:
	if isinstance(item,(int,float)) and not isinstance(item,bool):
		s+=item
		
print(s)
