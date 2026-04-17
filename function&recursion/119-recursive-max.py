def rmax(arr):
    if len(arr) == 1:
        return arr[0]

    m = rmax(arr[1:])
    return arr[0] if arr[0] > m else m


print(rmax([3, 9, 2, 7, 5]))