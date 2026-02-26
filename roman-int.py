def rti(r,i = 0,prev=0):
    if not r:
        return i
    values = {'i':1,'v':5,'x':10}
    curr = values[r[0]]
    i += curr
    if curr>prev:
        i-=2*prev
    return rti(r[1:],i,curr)
print(rti('xxiv'))
exit()
def rmn(r, s=0, prev=0):
    values = {
        'i': 1, 'v': 5, 'x': 10,
        'l': 50, 'c': 100,
        'd': 500, 'm': 1000
    }

    if not r:
        return s

    curr = values[r[0]]
    s += curr

    # if previous was smaller, fix the total
    if prev < curr:
        s -= 2 * prev

    return rmn(r[1:], s, curr)


print(rmn('xxxiv'))   # 34
print(rmn('iv'))      # 4
print(rmn('mcmxciv')) # 1994
exit()
#positive roman
last_result = None
def rmn(r,s=0):
    #global last_result
    #last_result = rmn()
    if r== '':
        return s

    if r[0] == 'i':
        s+=1
    elif r[0] == 'v':
        s+=5
    elif r[0]  == 'x':
        s+=10
    
    return rmn(r[1:],s)
print(rmn('xxxiv'))
exit()
def roman_to_int(rmn:str,s=0)->int:

    if rmn == '':
        return s
    if rmn[1]:
        if rmn[0]=='i' and rmn[1] not in ['v','x']:
            s+=1
    if rmn[0]=='i' and rmn[1] in ['v','x']:
        s-=1
    elif rmn[0]=='v':
        s+=5
    elif rmn[0] == 'x':
        s+=10
    return s + roman_to_int(rmn[1:],s)

print(roman_to_int('iii'))
