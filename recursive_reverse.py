"""Recursive reverse list using slicing"""
#key things: list attribute how they works, do they return or not
#priority is getting last item first then do what ever with it ,it will be reversed

"""recursive reverse list using slice"""
def recursive_reverse(array):#[1,2,4]#[1,2f]
	
	if array == []:
		return []
	first = array[-1]#4#2
	rest = array[0:len(array)-1]#[1,2]#1
	result = []
	result.append(first)#[4]#[2]
	return result+recursive_reverse(rest)#[6]+
print(recursive_reverse([1,2,3,4,5,6]))
"""Recursive reverse list using iteration"""	
def recursive_reverse(array,i = 0)-> list:#[1,2,3,4,5,6]
	
	if abs(i) == len(array):#0#1
		return []#as we want list as output
	return [array[i-1]]+recursive_reverse(array,i-1)#[6]+#[5]..	
"""RECURSIVE REVERSE USING TAIL RECURSION"""
#gpt
def recursive_reverse(array, acc=None):
    if acc is None:
        acc = []  # initialize accumulator
    
    if not array:  # base case: empty list
        return acc
    
    # take the last element and add it to accumulator
    acc.append(array[-1])
    
    # recurse on the rest of the list
    return recursive_reverse(array[:-1], acc)

print(recursive_reverse([1, 2, 3, 4, 5, 6]))

		
print(recursive_reverse([1,2,3,4,5,6]))

