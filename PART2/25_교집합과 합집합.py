n = int(input( ))
setn = list(map(int, input( ).split( )))
m = int(input( ))
setm = list(map(int, input( ).split( )))

s1 = [ ]
s2 = setm

for x in setn:
      if x in setm:
           s1.append(x)
      if x not in setm:
           s2.append(x)

if s1 == [ ]:
      print(0, end = '')
for x in sorted(s1):
      print("%d "%x, end = '')
print( )
for x in sorted(s2):
      print("%d "%x, end = '')
