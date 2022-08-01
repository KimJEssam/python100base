for i in range(s=0,1, 101):
    if i < 100:
        print(i, end = ' ')
    else:
        print(i)
    s += i
print("1부터 100까지의 합은 %d입니다." % s)
