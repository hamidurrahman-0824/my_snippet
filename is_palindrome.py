def reverse_string(s:str)->str:
	l = list(s)
	left,right = 0,len(s)-1
	while left<right:
		l[left],l[right]=l[right],l[left]
		left+=1
		right-=1
	return ''.join(l)
def rcr(s):
	
	if s=="":
		return ''
	
	return str(s)[-1]+rcr(str(s)[:-1])
print(rcr('majed'))
def is_palindrome(s:str)->bool:
	return rcr(s)==str(s)
print(is_palindrome(1234321))
