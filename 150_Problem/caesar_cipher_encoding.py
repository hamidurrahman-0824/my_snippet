def caesar_cipher_encod(s:str,ss:int)->str:
	en = ''
	for i in range(len(s)):
		if s[i] == ' ':
			
			en += s[i]
		
		else:
			ch = chr(ord(s[i])+ss%26)
			en += ch
			
	return en
print(caesar_cipher_encod('zchatgpt is not as good as claude',4))
def caesar_cipher_decod(s,ss):
	en = ''
	for i in range(len(s)):
		
		if s[i] == ' ':
			en += s[i]
		else:
			ch = chr(ord(s[i])-ss%26)
			en += ch
		
	return en
print(caesar_cipher_decod('~glexktx mw rsx ew kssh ew gpeyhi',4))
			
#(ord(char) - ord('a') + shift) % 26 + ord('a'), correct order
