#slicing
import numpy as np
arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]
                ])
#array[start:end:step]
print(arr[-1])#0-n,0:3,[:(all row),0(column)][row,column]
print(arr[:,0])
print(arr[0:2,0:2])
#arithmatic[+-*/]
print(arr[arr==5])
arr[arr<10] = 0
print(arr)
#broadcasting(any of 1 or same)#(1,3)(3,1)#read right to left
#
ar = np.array([[1,2,3,4]])
arr = np.array([[1],[2],[3],[4]])

# print(arr.shape)
# print(ar.shape)
# print(ar*arr)
a = np.array(5)#->(col,row)
b = np.array([1,2,3])#(col,row)->(row,col)
print(a.shape,b.shape)#(),(3,)->1,1-1,3
