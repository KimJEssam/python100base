data = input( )
dic = { }
for x in range(26):
   x = chr(ord('a') + x)
   dic[x] = 0
for x in data:
   if x in dic:
      dic[x] += 1
for x in range(26):
   x = chr(ord('a') + x)
   print("%c:%d" % (x, dic[x]))
