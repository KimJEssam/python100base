def f(x, y):
    if x > y:
        return x
    else:
        return y
    
a, b, c = map(int, input().split())
print(f(f(a, b), c))
