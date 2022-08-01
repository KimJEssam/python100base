a, b = input( ).split( )
a = int(a)
b = int(b)
sum = 0
for i in range(a, b + 1):
   if i%2 == 1:
       sum = sum + i
       if i == a:
            print(i, end = ' ')
       else:
            print("+%d" % i, end = ' ')
   else:
       sum = sum - i
       print("-%d" % i, end = ' ')
       
print("=%d" % sum)
