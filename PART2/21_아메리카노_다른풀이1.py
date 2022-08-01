def f(k, n):
    if k<n: 
      return 0
    return k//n + f(k//n+k%n, n)

k, n = input().split()
k = int(k)
n = int(n)

print( f(k, n) )