def f(x):
    if x == 1:
        return x
    else:
        return f(x-1)*x
    
n = int(input())
print(f(n))
