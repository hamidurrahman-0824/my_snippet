import numpy as np

exit()
arr = np.array([
				[
				[1,2,3],
				[11,12,13],
				[2,3,4]
				],
				[
				[14,15,16],
				[3,4,5],
				[17,18,19]
				]
				])#[[],[],[]]2d,[[[],[],[]], [[],[],[]]]3d
# print(arr.ndim)
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)
# print(arr[:,:3])
"""For 1D arrays, you only use one slice: arr[:3].

For 2D arrays, it’s arr[row_slice, column_slice].

For 3D arrays, you’d extend it: arr[depth_slice, row_slice, column_slice].

So arr[:,:3] is valid only if arr has at least 2 dimensions. If arr is 1D or scalar, you’ll get an error."""
"""
🔍 Indexing rules
1D array → single index: arr[i]

2D array → two indices: arr[row, column]

3D array → three indices: arr[depth, row, column]

In general: arr[i1, i2, i3, ...] where the number of indices matches arr.ndim."""
#0D
ar = np.array('a')
#1D
a1d = np.array([1,2,3])
#2d
ar2d = np.array([
    			[1,2,3],
                [2,3,4]
                ])
#3D
ar3d = np.array([[[],[],[]]])
print(ar3d.ndim)