
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))
def gcd(a,b):
    return a if b==0 else gcd(b,a%b)