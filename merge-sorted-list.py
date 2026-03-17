def merge_sorted(arr1,arr2)-> list:
	merged = []
	if len(arr1) == len(arr2):
		for i in range(len(arr1)):
			n = tuple(arr1[i],arr2[i])
			merged.append(n)
	elif len(arr1) < len(arr2):
		for i in range(len(arr1)):
			merged.extend([arr1[i],arr2[i]])
	else:
		for i in range(len(arr2)):
			merged.extend([arr1[i],arr2[i]])
	return merged
print(merge_sorted([1,3,5,7],[2,4,6]))
