k, n = input().split()
k=int(k)
n=int(n)

cnt=0
while k>=n:
  cnt=cnt+k//n
  k=k//n + k%n
print(cnt)