def f(p, s):
   global n, m, data, ans
   if p == n:
      if s == m:
         ans += 1
      return
   f(p + 1, s + data[p])
   f(p + 1, s - data[p])

   
m = int(input( ))
n = int(input( ))
if n != 0:
   data = list(map(int, input( ).split( )))
ans = 0

f(0, 0)
print(ans)
