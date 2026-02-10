number = 100.993456
round = 1
rounded = int(number*10**round+0.5)/10**round
#print(rounded)
def round_of_manually(num,dig):
    shift1 = num*10**dig
    shift = shift1+0.5#int(shift1+0.5)
    shifted = shift-shift%1
    return shifted/10**dig
#print(round_of_manually(3.13534,2))
def round_negative_number(num,dig):
    shift1 = num*10**dig
    shift = shift1-0.5
    shifted = shift-shift%1
    return shifted/10**dig
    
print(round_negative_number(-3.15779,2))
 