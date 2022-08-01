data = input( )
for x in range(26):
    x = chr(ord('a') + x)
    print("%c:%d" % ( x, data.count(x)))
