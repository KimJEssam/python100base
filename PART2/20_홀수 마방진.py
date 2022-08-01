n = int(input( ))

ms = [[0] * n for i in range(n)]
row = 0
col = n // 2

for v in range(1, n * n + 1):
   ms[row][col] = v
   if v % n == 0:
      row = (row + 1) % n
   else:
      row = (row - 1 + n) % n
      col = (col + 1) % n
for row in range(n):
   for col in range(n):
      print("%d "%ms[row][col], end = '')
   print( )
