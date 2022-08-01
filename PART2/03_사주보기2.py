y, m, d = input( ).split( )
y = int(y)
m = int(m)
d = int(d)
s = (y + m + d) // 100 % 10
if s%2 == 0:
     print("대박")
else:
     print("그럭저럭")
