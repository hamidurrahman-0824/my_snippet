def recursive_denesting(array):
	if array == []:
		return []
	first = array[0]
	rest = array[1:]
	if isinstance(first,list):
		return recursive_denesting(first)+recursive_denesting(rest)
	else:
		return [first]+recursive_denesting(rest)
print(recursive_denesting([[1],[2],[2,[2,[2]]]]))
#bot
import numpy as np

nested = [[1, 2], [3, 4], [5, 6]]
flat = np.array(nested).flatten().tolist()
print(flat)  # [1, 2, 3, 4, 5, 6]
