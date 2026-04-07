#Input: [8]
arr = [8, 3, 3,40, 1, 7, 0, 10, 20,30]

srt = []
def max(arr:list)->int:
    mx = 0
    for i in range(len(arr)):
        pass
def quicksort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([8,3,1,7,0,10,2]))
#
def quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    left = [x for x in a if x < pivot]
    mid = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quicksort(left) + mid + quicksort(right)


print(quicksort([8,3,1,7,0,10,2]))