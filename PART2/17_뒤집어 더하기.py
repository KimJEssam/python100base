def revnum(n):
   res = 0
   while n > 0:
      res = res * 10 + n % 10
      n = n // 10
   return res

n = int(input( ))

m = n + revnum(n)
if m == revnum(m):
      print("YES")
else:
      print("NO")
