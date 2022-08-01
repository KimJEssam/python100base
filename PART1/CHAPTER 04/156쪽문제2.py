def f(x):
    if x == 1:
        print("*", end = '')
    else:
        f(x-1)
        print("*", end = '')
    
n = int(input())
f(n)
