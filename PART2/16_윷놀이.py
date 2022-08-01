def yut(a, b, c, d):
     return a + b + c + d

a, b, c, d = map(int, input( ).split( ))

res = yut(a, b, c, d)
if res == 1:
         print("도")
elif res == 2:
         print("개")
elif res == 3:
         print("걸")
elif res == 4:
         print("윷")
else:
         print("모")
