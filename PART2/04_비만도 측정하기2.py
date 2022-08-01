h,w = input( ).split( )
h = float(h)
w = float(w)
if h < 150:
   stdw = h - 100
elif h < 160:
   stdw = (h - 150) / 2 + 50
else:
   stdw = (h - 100) * 0.9
bmi = (w - stdw) * 100 / stdw
if bmi <= 10:
   print("정상")
elif bmi <= 20:
   print("과체중")
else:
   print("비만")
