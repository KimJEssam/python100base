a, b = map(int, input( ).split( ))
era = [False, False] + [True] * (b - 1)

for x in range(2, b + 1):
    if era[x]:
        for j in range(x + x, b + 1, x):
            era[j] = False
            
for x in range(a, b - 1):
    if era[x] and era[x + 2]:
        print(x, x + 2)
