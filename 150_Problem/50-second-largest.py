def second_max(arr):
	mx = max(arr)
	new = [item for item in arr if item != mx]
	return max(new)
	
print(second_max([1,0,8,8,7,4,11,4,12,12,11]))
#chatgpt
def second_max(arr):
    return sorted(set(arr))[-2]
    
def second_max(arr):
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second

import heapq

def second_max(arr):
    return heapq.nlargest(2, set(arr))[1]
