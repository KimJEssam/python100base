n = input( )
n = int(n)

if 11 <= n <= 13:
     print("%dth" % n)
if n%10 == 1:
     print("%dst" % n)
if n%10 == 2:
     print("%dnd" % n)
if n%10 == 3:
     print("%drd" % n)
else:
     print("%dth" % n)
