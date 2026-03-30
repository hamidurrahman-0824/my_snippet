with open('gittroubleshots.txt','r') as file:
    seen = set()
    content = []
    for line in file:
        line = line.strip()
        if line not in seen:
            seen.add(line)
            content.append(line)
    
#regardless of order
with open('gittroubleshots.txt','r') as file:
    content = list({line.strip() for line in file})  
#modern trick with preserved order
with open('gittroubleshots.txt','r') as file:
    d = [line for line in file]#cursor at the end
    file.seek(0)#cursor back to zero pos
    content = list(dict.fromkeys(line.strip() for line in file))
    
    print(len(content),len(d))
#extras:enumerate(iterable, start),zip(iterable1, iterable2, ...)->make pair
"""zip()       → combine iterables
enumerate() → add index"""
