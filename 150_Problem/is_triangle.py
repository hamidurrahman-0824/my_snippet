def is_triangle(x:float,y:float,z:float)->bool:
	return (x>0 and y>0 and z>0) and (x+y>z and y+z>x and z+x>y)
if __name__=='__mane__':
	assert is_triangle(0,1,2) == False
	assert is_triangle(-2,1,2) == False
	assert is_triangle(9,1,2) == False
	assert is_triangle(3,4,5) == True
	print('all test passed')
	
