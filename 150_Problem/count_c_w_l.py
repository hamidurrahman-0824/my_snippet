def line_count(file):
	s = 0
	with open(file,'r+') as f:
		for line in f:
			s+= 1
	return f"Total line = {s}"
print(line_count('/media/dwgls/SSD/DOWNLOAD/abcdef'))
def word_count(file):
	s = 0
	with open(file, 'r') as f:
		for line in f:
			for word in line.split():
				s+=1
		return f"Total word = {s}"
def ch_count(file):
	ms = 0
	chs = 0
	ns = 0
	pn = 0
	pnn = []
	with open(file,'r') as f:
		for line in f:
			for ch in line:
				ms +=1
				if ch.isalpha():
					chs+=1
				elif ch.isdigit():
					ns += 1
				else:
					pnn.append(ch)
					pn+=1
		string = f"Uniq punc. = {len(set(pnn))},overall punctuation = {len(pnn)}\nTotal mass character= {ms}\nTotal alphabet = {chs}\nTotal digit = {ns}\nTotal punctuation = {pn}"
		return string
print(ch_count('/media/dwgls/SSD/DOWNLOAD/abcdef'))

print(word_count('/media/dwgls/SSD/DOWNLOAD/abcdef'))	

#chatgpt
import string

def ch_count(file):
    ms = chs = ns = pn = 0
    unique_punc = set()

    with open(file) as f:
        for line in f:
            for ch in line:
                ms += 1
                if ch.isalpha():
                    chs += 1
                elif ch.isdigit():
                    ns += 1
                elif ch in string.punctuation:
                    pn += 1
                    unique_punc.add(ch)

    return f"""Unique punctuation = {len(unique_punc)}
Overall punctuation = {pn}
Total characters = {ms}
Total alphabets = {chs}
Total digits = {ns}"""
exit()
def has_https(link):
	return 'https://' in link
import re

def is_email(email):
	pattern = r'^[A-Za-z0-9-.%]+@[A-Za-z0-9]+\.[A-Za-z]{2,}$'
	return bool(re.match(pattern,email))
def has_email(email):
	return bool('@' in email)
with open('/media/dwgls/SSD/DOWNLOAD/abcdef','r+') as file:
	emails = []
	for line in file:
		if has_email and is_email(line):
			new = line.strip('\n')
			emails.append(new)
	print(emails)
with open('/media/dwgls/SSD/DOWNLOAD/abcdef', 'r+') as file:
	links = []
	for line in file:
		if has_https(line):
			new = line.strip('\n')
			links.append(new)
	print(set(links))
	print(len(set(links)))

with open('/media/dwgls/SSD/DOWNLOAd/abcdef','r+') as f:
	s = 0
	for line in f:
		if line.strip() == '' or not line.strip().isalpha():
			s+=1
	print(s)
	
exit()
with open('/media/dwgls/SSD/DOWNLOAD/abcdef','r+') as file:
	s = 0
	for line in file:
			s+=1
	print(f"Line = {s}")
	a = 0
	for line in file:
		for word in line.split():
			a+=1
	print(f"word = {a}")
	b = 0		
	for line in file:
		for ch in line:
			if ch.isalpha():
				b+=1
	print(b)
	
