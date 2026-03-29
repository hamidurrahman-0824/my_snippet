#consider every item is pure int:
def sum_pure_int(arr):
	s = 1
	n0 = 0
	for item in arr:
		if item ==0:
			n0+=1
			
		elif isinstance(item,(int,float)):
			s+=item
	return f"""Sum of this array = {s}
{n0} zero(s) found and escaped."""
print(sum_pure_int([1,2,3,4,5,6,7,7,9,1,0,0,0.2]))
#sum of all possible item
#boolean depend on intention, bool part canbe removed
def robust_sum(arr:list)->int:
	if not arr:
		return "List not found"
	s = 0
	nb=0
	nn = 0
	tnb = 0
	for item in arr:
		if isinstance(item,bool):
			if item:
				tnb+=1
			nb+=1
			s += item
		elif isinstance(item,(int,float)):
			s += item
		elif item.isdigit():
			s += int(item)
		else:
			nn+=1
	return f"""Sum of this array = {s}
{nb} boolian(s) found only {tnb} values are True and added
{nn} item(s) not added due to their non-alligned class"""
print(robust_sum([1,2,3,4,'abc','1233',True,False,0,'1','!','#',1.2,0.22]))
