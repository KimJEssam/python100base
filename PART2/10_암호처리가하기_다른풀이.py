str = input() 
se1 = []
se2 = []
for x in str:
  se1.append(chr(ord(x)+2))
  se2.append(chr(ord(x)*7%80+48))
print(''.join(se1))
print(''.join(se2))