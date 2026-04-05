from collections import defaultdict,Counter
with open('repository_creation.txt','r',encoding='utf-8') as file:
    freq = {}
    for line in file:
        for word in line.lower().split():
            word = word.strip("().,!?;:\"'")
            freq[word] = freq.get(word,0)+1
    revrs = defaultdict(list)
    for k,v in freq.items():
        revrs[v].append(k)
    print(max(revrs),revrs[max(revrs)])    
    print(revrs)
#    print(freq)
with open('repository_creation.txt','r',encoding='utf-8') as file:
    longest = ""
    for line in file:
        for word in line.lower().split():
            word = word.strip("().,!?;:\"'")
            if len(word)>len(longest):
                longest = word
print(longest,len(longest))