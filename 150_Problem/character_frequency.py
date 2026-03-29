def vowels(s):
	v = 0
	for ch in s:
		if ch.lower() in "aeiou":
			v+=1
	return v
def cons(s):
	c= 0 
	for ch in s:
		if vowels(ch):
			continue
		elif ch.isalpha():
			c+=1
	return c
def vowcon(s):
	return f"cons:{cons(s)}\nvowels:{vowels(s)}"
#print(vowcon('the quick brown fox jumps over the lazy dogs'))
from collections import Counter

def char_freq(s):
	r = 0
	for ch in s:
		if ch.isalpha():
			r+=1
		else:
			continue
def freq(s):
	return Counter(s)
def anagram(s1:str,s2:str)-> bool:
	return freq(s1)==freq(s2)
def own_counter(s:str)-> dict:
	result = {}
	for ch in s:
		if ch not in result:
			result[ch]=1
		else:
			result[ch]+=1
	return result
	"""Need some robust conditon there"""
def is_anagram(s1,s2):
	return own_counter(s1)==own_counter(s2)
#print(is_anagram('silent','car'))
def angrm(s1,s2):
	l1 = sorted(list(s1))
	l2 = sorted(list(s2))
	return l1==l2
	
print(angrm('silent','listen'))
print(angrm('jar','car'))

