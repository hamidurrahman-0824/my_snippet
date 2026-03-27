import numpy as np
a = np.arange(12).reshape(3,4)
print(a)
print(a[1,2])
print(a[:,1])
a = np.array([2,5,8,1,9])
print(a[a > 5])
a = np.arange(1,11)
b = a[a>5]*2
print(b)
A = np.array([[1,2,3],
              [4,5,6]])

b = np.array([10,20,30])
print(A+b)
print(b)
print(b.shape)
exit()
#linspace
arr = np.linspace(0,1,5) #start,stop, number of elements
#with specific value
full = np.full(5,7)
identity= np.eye(3)
print(identity)
random_ar = np.random.rand(5)#uniform distirubution[0,1])
random_int = np.random.randint(1,10,size=5)
#reshape(2,-1[will handle auto])
#where is search,it gives indics/index

A = np.array([[1,2,3],
              [4,5,6]])#(2,3)

b = np.array([10,20,30])#(,3)


A + b
