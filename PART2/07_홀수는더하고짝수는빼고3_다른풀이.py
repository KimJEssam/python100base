a, b = input().split()
a = int(a)
b = int(b)

sum=0
i=a
while (i <= b):
    if i%2 == 1:
        sum = sum + i
        if i == a:
            print(i, end='')
        else:
            print("+%d"%i, end='')
    else:
        sum = sum-i
        print("-%d"%i, end='')
    i+=1
print("=%d"%sum)
