#axis: one direction,axes: collection of all directions
import numpy as np
a = np.array([20,10,30])
print()
c = np.ones((2,3,4))
print(c)
b = np.array([[1, 2, 3],[4, 5, 6]])
print(b.shape)
b = np.array([[[1,2],[2,3],[3,0]],[[2,0],[3,0],[7,0]]])#2,3,2
b = np.array([[[1,2],[2,3],[3,0]],
               [[2,0],[3,0],[7,0]]])#2,3,2
print(b.shape)
print(np.sum(b,axis=0))#[[1,2],[2,3],[3,0]],[[2,0],[3,0],[7,0]]
print(np.sum(b,axis=1))#[[1,2],[2,3],[3,0]*[2,0],[3,0],[7,0]]->2x2
print(np.sum(b,axis=2))#[[1,2*2,3*3,0],[2,0*3,0*7,0]]
