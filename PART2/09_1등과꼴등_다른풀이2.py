n = int(input())
data = map(int, input().split())
data = list(data)
data.sort()
print(data[-1], data[0])
