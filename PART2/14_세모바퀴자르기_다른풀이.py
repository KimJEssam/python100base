n = int(input())

cnt=0
for a in range(1, n+1):
  for b in range(a, n+1):
    c=n-(a+b)
    if c>=b and a+b>c:
        print(a, b, c)
        cnt=cnt+1

if cnt==0:
  print(-1)