import math
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

n = math.gcd( math.gcd(a, b), c )
print(n)