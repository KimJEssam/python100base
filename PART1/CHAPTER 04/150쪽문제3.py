def f(x, y):
    if x > y:
        return x
    else:
        return y
    
s = [18, 77, 68, 54, 99, 15, 56, 97, 64, 48]
mx = 0
for x in s:
    mx = f(mx, x)
print(mx)
