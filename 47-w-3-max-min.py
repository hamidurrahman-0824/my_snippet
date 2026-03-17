arr = [1,2,13,4,5,6,7,7,8,48,8]
def max_(ar):
	if not ar:
		return 0
	mx = 0
	for i in range(len(ar)-1):
		if ar[i]>ar[i+1]:
			mx = arr[i]
		else:
			mx = arr[i+1]
	return mx
def min_(ar):
	if not ar:
		return 0
	mn = ar[0]
	for i in range(len(ar)-1):
		if ar[i+1] > mn:
			ar[i+1] = mn
	return mn
print(min_([1,2,13,4,5,6,-1,7,7,8,48,8]))

mn = arr[0]
mx = arr[0]
for i in arr:
	if i>mx:
		mx = i
	else:
		mx = mx
print(f"(max,min) = {mx,mn}")
#chatgpt
def find_max_min(arr):
    mx = mn = arr[0]

    for num in arr[1:]:
        if num > mx:
            mx = num
        elif num < mn:
            mn = num

    return mx, mn
