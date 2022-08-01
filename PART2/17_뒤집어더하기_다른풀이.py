n = int(input())

sum = n + int(str(n)[::-1])
if sum == int(str(sum)[::-1]):
    print("YES")
else:
    print("NO")