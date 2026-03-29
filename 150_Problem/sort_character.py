def sort_character(s):
    
    return ' '.join(''.join(ch for ch in sorted(word,key= str,reverse=False)) for word in s.split(' '))
print(sort_character("data science is fun.but playing"))
a = 'asdf.string '
cd = a.split()
b = ' '.join(''.join(ch for ch in word) for word in cd)
print(b)