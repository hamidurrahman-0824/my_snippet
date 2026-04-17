def power_set(arr):
    if not arr :
        return [[]]
    first= arr[0]
    rest = power_set(arr[1:])
    with_first = []
    for subset in rest:
        with_first.append([first]+subset)
    return rest + with_first
print(power_set([2,1]))

def power_set(arr):
    if not arr:
        return [[]]

    rest = power_set(arr[1:])
    return rest + [[arr[0]] + subset for subset in rest]


print(power_set([1,2,3]))