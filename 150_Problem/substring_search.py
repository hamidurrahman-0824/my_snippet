def subs(s,sb):
	return s.count(sb)
print(subs('iiiiiiii','i'))
#using regex
import re
def subs(s,sb):
	return re.findall(sb,s)
def subs_occurrence(s, sub):
    return sum(s[i:i+len(sub)] == sub for i in range(len(s)-len(sub)+1))
def subs(s,sb):
	return sum(sub==s[i:i+len(sb)] for i in range(len(s)))
def subocr(s,sub):
	sm = 0
	for i in range(len(s)-len(sub)+1):
		if sub == s[i:i+len(sub)]:
			sm+=1
	return sm
print(subocr('aaaaaaa', 'a'))

exit()
def subs_search(s,sub):
	return bool(sub in s)
print(subs_search('majedmajedmajed','ma'))
def subs_occurence(s,sub):
	x = len(s)
	y = len(sub)
	if x<y:
		return "Invalid substring"
	
	sm = 0
	prev,nxt = 0,y
	for _ in range(0,x,y):
		if s[prev:nxt]==sub:
			sm +=1
		prev,nxt = nxt,nxt+y
		if nxt>x:
			return sm
print(subs_occurence('the world is changing very fast','r'))
def subs_occurence(s, sub):
    x = len(s)
    y = len(sub)
    if x < y:
        return "Invalid substring"
    
    sm = 0
    for i in range(x - y + 1):
        if s[i:i+y] == sub:
            sm += 1
    return sm

print(subs_occurence('the world is changing very fast', 'is'))  # 1
print(subs_occurence('the world is changing very fast', 'r'))   # 1
print(subs_occurence('mississippi', 'ss'))  # 2
def subs_occurrence(s, sub):
    return sum(s[i:i+len(sub)] == sub for i in range(len(s)-len(sub)+1))
