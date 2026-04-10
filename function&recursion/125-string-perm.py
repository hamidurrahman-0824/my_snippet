#a->a,a,b->a,b,b,a
string = '12345'
newstr = string+string
perm = []
for i in range(len(string)):
    perm.append(newstr[i:len(string)+i])

def permute(s):#
    if len(s) == 1:
        return [s]

    result = []
    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i+1:]        
        for p in permute(remaining):
            result.append(char + p)
    return result


print(permute("ABC"))
from itertools import permutations

s = "ABC"
result = permutations(s)

for p in result:
    print("".join(p))
   
