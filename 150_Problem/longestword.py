def counter(sentence):
    dic = {}
    lst = sentence.split()
    for item in lst:
        if item not in dic:
            dic[item] = len(item)

    return dic
words = "the qucik brown fox monkey rungee kkutta jumps over the lazy dogs cat"
s = sorted(list(words.split()),key=len)
mx = max(s,key=len)#monkey
mxln = len(mx)

for item in s:
    if len(item) == mxln:
        print(item)
exit()
print(s)
def longest_word(sentence:str)->str:
    dic = counter(sentence)
    mx = max(dic.values())
    for k,v in dic.items():
        if v == mx :
            return f"Longest word :{k}\nLength:{v}"
        
    if not dic:
        return -1
    
#print(longest_word(words))
#chatgpt
def longest_word(sentence: str) -> str:
    words = sentence.split()

    if not words:
        return -1

    longest = max(words, key=len)
    return f"Longest word: {longest}\nLength: {len(longest)}"


print(longest_word("the qucik brown fox monkey jumps over the lazy dogs cat"))