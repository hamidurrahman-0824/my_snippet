arr = ['1',["a"],[['b'],['c']]]
def rcr_flat(arr):
    if not arr:
        return []
    cur = arr[0]#1,
    rest = arr[1:]#['a'...]

    if isinstance(cur,list):
        return rcr_flat(cur) + rcr_flat(rest)
    else:
        return [cur] + rcr_flat(rest)#[1]+["a"...]
print(rcr_flat(arr))
