def title_man(name):
    n = name.split()
    rr = ''
    for i in n:
        r = i.strip()
        r = i[0].upper() + ''.join(ch for ch in i[1:])
        rr += r+' '#produce extra space at the end
    return rr.strip()
print(title_man(" multiple  spaces  "))
print(title_man("john's book"))
def title_man(name):
    words  = name.split()
    result = ''
    for w in words:
        result+= w[0].upper()+ w[1:] + ' '
    return result.strip()
print(title_man('the man of honour'))

def pythonic_title_case(name):
    return ' '.join(w[0].upper()+w[1:] for w in name.split())
print(pythonic_title_case("john's book"))
print(pythonic_title_case(" multiple  spaces "))