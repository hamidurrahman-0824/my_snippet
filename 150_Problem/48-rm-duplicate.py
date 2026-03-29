def rm_duplicate(arr:list)->list:
	uniq_arr = []
	if not arr:
		return []
	for item in arr:
		if item not in uniq_arr:
			uniq_arr.append(item)
	return uniq_arr
#chatgpt
def remove_duplicates(arr):
    seen = set()
    result = []

    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result
    
def remove_duplicates(arr):
    return list(dict.fromkeys(arr))

def remove_duplicates(arr):
    seen = set()
    result = []

    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result
