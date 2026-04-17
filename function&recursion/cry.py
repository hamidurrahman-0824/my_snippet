s='ab'
"""
a,A
b,B
i=0->ab->ab,AB aB,aB,Ab,AB
"""
def letter_perm(s):
	if len(s)==1:
		return [s]+[s.upper()]
	result = []
	first = letter_perm(s[0])
	
	rst = s[1:]
	for i in first:
		for j in letter_perm(rst):
			result.append(i+j)
	return result
	
print(letter_perm('ab'))

def fixed_letter_perm(s):
	if len(s)==0:
		return [""]
	result = []
	ch = s[0]
	rst = s[1:]
	choices= [ch.lower(),ch.upper()] if ch.isalpha() else [ch]
	
	for c in choices:
		for p in fixed_letter_perm(rst):
			result.append(c+p)
	return result
	
print(fixed_letter_perm('a1b'))
def anoi(n,source,helper,destination):
	if n==1:
		print(f"{n} disk moved to {destination} from {source}")#direct move from src to dest
		return
	anoi(n-1,source,destination,helper)#src->dest(helper)
	print(f"{n-1} moved to {helper} from {source}")
	anoi(n-1,helper,source,destination)#src(helper)->dest
anoi(3,"a","v","c")