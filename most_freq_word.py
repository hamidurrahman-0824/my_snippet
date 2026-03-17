text = 'majedtdsbdsdfghjkerthjkasdfghjo1234'
from collections import Counter
num = ''.join(ch for ch in text if ch.isalpha())
print(Counter(num))
mx = 0
d =Counter(num).items()

for k,v in d:
	if v>mx:
		mx = v
	print(f"{d[k]},{mx}")
	
	
