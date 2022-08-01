s = [18, 77, 68, 54, 99, 15, 56, 97, 64, 48]
for i in range(0, 9):
    for j in range(i+1, 10):
        if s[i] > s[j]:
            t = s[i]
            s[i] = s[j]
            s[j] = t
for i in range(0, 10):
    print(s[i], end = ' ')
