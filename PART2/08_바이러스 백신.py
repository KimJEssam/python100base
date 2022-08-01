a, b, c = input( ).split( )
a = int(a)
b = int(b)
c = int(c)
for i in range(a, 0, -1):
    if a % i == 0 and b % i == 0 and c % i == 0:
       g = i
       break
print(g)
