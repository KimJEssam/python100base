a, b = input().split()
c, d = input().split()
e, f = input().split()

a=float(a)
c=float(c)
e=float(e)
b=int(b)
d=int(d)
f=int(f)

s=a*b+c*d+e*f
print("{:.1f}".format(s))