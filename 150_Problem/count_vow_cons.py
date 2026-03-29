def count_vow_con(string):
	vow,con=0,0
	for ch in string:
		if ch in 'aeiouAEIOU':
			vow+=1
		elif ch.isalpha():
			con+=1
	return vow,con
print(count_vow_con('MaJED'))
def man_count(string):
	vow,con=0,0
	for ch in string:
		if ch in 'aAeEiIoOuU':
			vow+=1
		elif ('a'<=ch <='z' or 'A'<=ch<='Z'):
			con+=1
	return vow,con
print(man_count('astagfirullahCOMEONMAN'))

from collections import Counter
def count_vowcon(string):
	total = Counter(string)
	vow = 0
	con = 0
	for k,v in total.items():
		if k in "aeiouAEIOU":
			vow+=v
		elif ('a'<=k<='z' or 'A'<=k<='Z'):#k.isalpha() is better for readability
			con+=v
	return vow,con
print(count_vowcon('12354i'))

# Input string
text = "Hello World"

# Define vowel and consonant lists
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [ch for ch in "abcdefghijklmnopqrstuvwxyz" if ch not in vowels]

# Convert text to lowercase for uniform comparison
text = text.lower()

# Count vowels using sum() with condition
vowel_count = sum(1 for ch in text if ch in vowels)

# Count consonants using sum() with condition
consonant_count = sum(1 for ch in text if ch in consonants)

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)


