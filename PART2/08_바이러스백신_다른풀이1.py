def gcd(a, b):
    mod = a%b
    while mod > 0:
        a = b
        b = mod
        mod = a%b
    return b

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print( gcd( gcd(a, b), c ) )
