n = input( )
n = int(n)
if 11 <= n <= 13:
    print("%dth" % n)
elif n%10 == 1:
    print("%dst" % n)
elif n%10 == 2:
    print("%dnd" % n)
elif n%10 == 3:
    print("%drd" % n)
else:
    print("%dth" % n)
