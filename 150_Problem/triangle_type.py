def greater_than_zero(x:float,y:float,z:float)->bool:
	return x>0 and y>0 and z>0
def is_triangle(x:float,y:float,z:float)->bool:
	if  greater_than_zero(x,y,z):
		return x+y>z and y+z>x and z+x>y

def triangle_type(x:float,y:float,z:float)-> str:
	if not is_triangle(x,y,z):
		return "Not a triangle."
	arms = {x,y,z}
	if len(arms) == 3:
		return "Scalene triangle"
	elif len(arms) == 2:
		return "Isosceles triangle"
	else:
		return "Equilateral triangle"
	
import is_triangle as it
print(it.is_triangle(5,5,9))
if __name__=='__main__':
	print(triangle_type(10,12,23))
def is_triangle(x: float, y: float, z: float) -> bool:
    # Positive sides + triangle inequality
    return (x > 0 and y > 0 and z > 0) and (x + y > z) and (y + z > x) and (z + x > y)

def triangle_type(x: float, y: float, z: float) -> str:
    if not is_triangle(x, y, z):
        return "Not a triangle."
    
    arms = {x, y, z}
    if len(arms) == 3:
        return "Scalene triangle"
    elif len(arms) == 2:
        return "Isosceles triangle"
    else:
        return "Equilateral triangle"

if __name__ == '__main__':
    # Quick test suite
    assert triangle_type(10, 12, 23) == "Not a triangle."
    assert triangle_type(7, 10, 12) == "Scalene triangle"
    assert triangle_type(5, 5, 8) == "Isosceles triangle"
    assert triangle_type(6, 6, 6) == "Equilateral triangle"
    assert triangle_type(-3, 4, 5) == "Not a triangle."
    assert triangle_type(0, 5, 5) == "Not a triangle."

    print("All tests passed!")
