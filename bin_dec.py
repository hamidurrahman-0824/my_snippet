
def dec_to_bin(n:int)->str:
	if n==0:
		return '0'
	forced_reversed = ''
	while n>0:
		reminder = n%2
		forced_reversed = str(reminder)+forced_reversed
		n//=2
	return forced_reversed
print(dec_to_bin(10012))
def bin_dec(n:str)->int:
	decimal = 0
	index = 0
	for i in range(len(n)-1,-1,-1):
		decimal += int(n[index])*2**i
		index += 1
	return decimal
print(bin_dec('101011'))

exit()
#2|11|5,10
def bn(n):
	bl = []
	while n>0:#n=11,n=5
		reminder = n%2
		bl.append(reminder)
		n = n//2#n=5
	return ''.join(str(i) for i in reversed(bl))
print(bn(11))

def d_b(n):
	if n==0:
		return '0'
	binary = ""
	while n>0:
		reminder = n%2
		binary = str(reminder)+ binary# 0+"",1+0+"" every time it get reversed
		n//=2
	return binary
#chatgpt#all type are in str, binary are not another type, it is just representation

num = 10
binary = bin(num)

print(binary)        # 0b1010
print(type(binary))  # <class 'str'>
num = 10
binary = format(num, 'b')

print(binary)   # 1010
#cleanest
num = 10
binary = f"{num:b}"

print(binary)   # 1010
#
print(bin(-10))        # -0b1010
print(format(-10, 'b'))  # -1010
