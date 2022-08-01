import sys
sys.setrecursionlimit(5000)

def f(k, n):
     if k < n:
         return 0
     return 1 + f(k - n + 1, n)

k, n = map(int, input( ).split( ))
print(f(k, n))
