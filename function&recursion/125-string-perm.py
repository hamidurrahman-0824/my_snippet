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


#print(permute("ABC"))
from itertools import permutations

s = "ABC"
result = permutations(s)

#for p in result:
#    print("".join(p))
"""i=0
-ch=a,rmn=bc,len=2
	i=0,ch=b,rmn=c->[c]
	i=1,ch=c,rmn=b->[b]
	for p in [c][b]
		

"""  
def prm(s):
	if len(s) == 1:
		return [s]
	result = []
	for i in range(len(s)):#3(0->ch->a,rmn->bc,prm(rmn)->),
		ch = s[i]#a
		rmn = s[:i]+s[i+1:]#bc
		for p in prm(rmn):#prm(bc)->ch=b,rmn=c->prm(rmn=c)->[c]
			result.append(ch+t)#
	return result
print(prm('abc'))
def permut(s):
	if len(s)== 1:
		return [s]
	result = []
	for i in range(len(s)):
		
