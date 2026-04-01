import re
string = '01342400777 01342400777 01342400777 01342400777 '
pattern = r'01[3-9]\d{8}'
print(re.findall(pattern,string))
exit()
# This finds all sequences of digits (1 or more)
#numbers = re.findall(r'\d+', text)
with open("phone_numbers.txt",'r') as f,\
    open('extracted_phone.txt','w') as out:
    for line in f:
#        line = line.strip()
        if is_phone(line):
            out.write(line)
##
import re

pattern = r'01[3-9]\d{8}'

with open("phone_numbers.txt") as f, \
     open("extracted_phone.txt","w") as out:

    for line in f:
        numbers = re.findall(pattern, line)
        for num in numbers:
            out.write(num + "\n")
##optional
import re

pattern = r'''
(?P<phone>\+?\d{7,15}) |
(?P<email>[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}) |
(?P<url>https?://\S+)
'''

regex = re.compile(pattern, re.VERBOSE)

text = "Call +8801712345678 or email test@mail.com visit https://example.com"

for m in regex.finditer(text):
    if m.group("phone"):
        print("Phone:", m.group("phone"))
    elif m.group("email"):
        print("Email:", m.group("email"))
    elif m.group("url"):
        print("URL:", m.group("url"))