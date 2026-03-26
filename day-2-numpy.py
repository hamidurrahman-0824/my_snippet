import numpy as np
#creating arrays
zeros = np.zeros((2,3),dtype='str')#arg: list,tuple,int
ones = np.ones([3,3])
empt = np.empty([3,3])#random value
arange = np.arange(2,15,3)#range
equal_interval = np.linspace(0,10)

#adding,removing,sorting
arr = np.array([7,8,9,0])
# print(np.sort(arr))
a = np.zeros(2,dtype=str)
b = np.arange(5,dtype=np.int64)
c = np.concatenate((a,b))
# print(c)
#reshape
a = np.arange(6)
# print(a)
b = a.reshape(3,2)
# print(b)
b = np.reshape(a,shape=(2,3),order='C')
x = np.arange(1, 25).reshape(2, 12)
# print(x)
#
x = np.array([[1, 2],[3,4]])
y = np.array([[5,6]])
z = np.concatenate((x,y), axis=0)
# print(z)
#conversion,D->another D
a = np.arange(7)
a2 = a[np.newaxis,:]
a3 = a2[np.newaxis,:]
# print(a3)
# print(a3.shape)
#
c = np.arange(11)
five_up = (c>5) | (c == 5)
# print(c[five_up])
#slicing and indexing, np.vstack(), np.hstack(), np.hsplit(), .view(), copy()
a,b = np.arange(5),np.arange(5,10)
# print(a)
# print(b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a+b)
#broadcasting
miles = np.array([1,2])
km = miles*1.6
print(km)
data = np.array([1,2],[2,5],[5,2])

