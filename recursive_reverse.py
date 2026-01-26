lst = [1,11,22,33,44,55]
def recursive_reverse(array,i=-1):
    if i == len(array) or array == []:
        return []
    first = array[0]
    rest = array[1:]

    return recursive_reverse(rest,i+1)
r = []
print(len(r))   
#print(recursive_reverse(lst))#[[[[[[[[]]]]]]]]