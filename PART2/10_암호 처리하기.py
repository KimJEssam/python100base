str = input( )
for x in str:
    print(chr(ord(x) + 2), end = '')
print( )
for x in str:
    print(chr(ord(x) * 7 % 80 + 48), end = '')
