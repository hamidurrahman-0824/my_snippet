def recursive_nested_list(arr):
	if arr == []:
		return []
	first = arr[0]
	rest = arr[1:]
	if isinstance(first,list):
		return recursive_nested_list(first)+recursive_nested_list(rest)
	return [first]+recursive_nested_list(rest)
nest = [1,[2],[2]]
print(recursive_nested_list(nest))
def recursive_nested_list(array):
	pass
#	return [item]+[nextitem]
		
nest = [1,[2],[2]]
print(recursive_nested_list(nest))
nest = [1,2,[2]]
temp = []
plainlst = []
for item in nest:
	if isinstance(item,list):
		temp = []
		temp.extend(item)
		for i in temp:
			if isinstance(i,list):
				temp.extend(i)
	else:
		plainlst.append(item)
print(plainlst)
	
a = [[2]]
b = [2]
a.extend(b)
print(a)
