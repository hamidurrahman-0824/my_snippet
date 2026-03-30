with open('repository_creation.txt','r',encoding='utf-8') as file:
    content = list(dict.fromkeys(line.strip() for line in file if line.strip()))
    content = sorted(content,key=len)#eq:key=lambda x:len(x))
    print(content)
words = ["apple", "Banana", "cherry"]
sorted(words, key=str.lower)  # ['apple', 'Banana', 'cherry']
sorted(words, key=len)        # ['apple', 'Banana', 'cherry'] (length 5,6,6)

data = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
sorted(data, key=lambda x: x[1])  # sort by score

from datetime import datetime

dates = ["2026-03-30", "2025-12-01", "2026-01-15"]
sorted(dates, key=lambda x: datetime.strptime(x, "%Y-%m-%d"))

data = [("Alice", 85), ("Bob", 90), ("Charlie", 85)]
sorted(data, key=lambda x: (x[1], x[0]))  # by score, then by name

with open('repository_creation.txt','r',encoding='utf-8') as file:
    content = list(dict.fromkeys(line.strip() for line in file if line.strip()))#avoids mt line
    content = sorted(content, key=lambda x: x.lower())
    with open('empty.txt','w+',encoding='utf-8') as dst:

        data = ''.join(line for line in content)
        dst.write(data)
        dst.seek(0)
        for line in dst:
            print(line)

"""
Quick “intermediate Python” cheatsheet
str.lower → case-insensitive
len → length of string/list
abs → numeric absolute
lambda x: x[i] → tuple/list element
lambda x: x.strip() → remove whitespace
lambda x: x.split()[-1] → last word
lambda x: (-x[1], x[0]) → descending numeric, then name
"""
"""
Key	Purpose
key=lambda x: x.strip()	Remove whitespace when sorting
key=lambda x: x.split()[0]	Sort by first word
key=lambda x: x.split()[-1]	Sort by last word
key=lambda x: x[::-1]	Sort by reversed string
"""