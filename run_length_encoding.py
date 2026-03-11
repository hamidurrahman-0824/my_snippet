from collections import Counter
def run_length_encoding(s):
	c = Counter(s)
	encod = ''
	for k,v in c.items():
		encod += f"{str(v)+k}"
	return encod
print(run_length_encoding('aaaabbbcddd'))

def run_length_decoding(s):
	c = ''
	for i in range(0,len(s)-1,2):
		c += f"{int(s[i])*s[i+1]}"#
	return c

print(run_length_decoding('4a3b1c3d'))
def run_length_encoding(s):
    encoded = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            encoded += str(count) + s[i-1]
            count = 1

    encoded += str(count) + s[-1]
    return encoded

def run_length_decoding(s):
    decoded = ""
    
    for i in range(0, len(s), 2):
        decoded += int(s[i]) * s[i+1]
    
    return decoded
