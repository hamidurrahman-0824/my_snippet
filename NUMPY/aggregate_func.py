#arg:max,min,mean,std,var,argmin(location of min),argmax,
#print(np.func(arg))
import numpy as np
arr = np.array([[1,2,4],
               [3,6,7]])
# print(np.sum(arr,axis=0))
# print(np.sum(arr,axis=1))
#filtering
import numpy as np

a = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])
rng = np.random.default_rng(seed=1)#->seed:reproduce same result
print("Dice",rng.integers(low=1,high=7,size=3))#size=(3,2)[for 3row,2cols ]
print("Dice",rng.integers(low=1,high=7,size=3))#size=(3,2)[for 3row,2cols ]

np.random.seed(seed=1)
print(np.random.uniform(low=-1,high=1,size=3))
rng = np.random.default_rng()

ar = np.array([1,2,3,4,5])
rng.shuffle(ar)
print(ar)
emojis = ['🤣','👌','❤️','😒','😂']
emoji = rng.choice(emojis,size=(3,3))
print(emoji)

#3D array = list of 2D arrays,tensor = stack of matrices