def reverse_string(string):
    return string[::-1]
def reverse_string(string):
    temp = list(string)
    result = ''.join(ch for ch in reversed(temp))
    return result
# print(reverse_string('majed'))
def reverse_without(string):
    a,b = '',''
    for ch in string:#m,,a
        a,b = ch,a#m,m
        b+=a   #mm            
    return b
    '''a = ''
for ch in string:
    a, ch = ch, a
    a = ch + a
return a
'''
print(reverse_without('matrix'))

def reverse_string(s):
    chars = list(s)
    i, j = 0, len(chars) - 1

    while i < j:
        chars[i], chars[j] = chars[j], chars[i]
        i += 1
        j -= 1

    return "".join(chars)
