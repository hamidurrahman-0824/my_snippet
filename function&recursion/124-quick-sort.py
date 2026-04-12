
arr = [8, 3, 3,40, 1, 7, 0, 10,-1,0,-3, 20,30]

def quicksort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]#8
    left = [x for x in arr[1:] if x <= pivot]#3,3,1,7,0|3-3,1,0|3-1,0|1-0
    right = [x for x in arr[1:] if x > pivot]#40,10,20,30|7

    return quicksort(left) + [pivot] + quicksort(right)


#print(quicksort(arr))
#
def quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    left = [x for x in a if x < pivot]
    mid = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quicksort(left) + mid + quicksort(right)

def qs(a):
    if len(a) <= 1:
        return a 
    piv = a[0]#3|
    l = [i for i in a[1:] if i<=piv]#2,1|
    r = [i for i in a[1:] if i>piv]#4|
    return qs(l)+[piv]+qs(r)#qs([2,1])+3+4
print(qs([3,2,1,4]))
#how it works
def q(a=[2,3,1]):
    if len(a) == 1:
        return a
    pivot= a[0]#1
    left = [x for x in a[1:] if x<=pivot]#[]
    right = [x for x in a[1:] if x>pivot]#>[2,3]
    return left+[pivot]+q(right)
print(q())