num = list(map(int, input().split()))
graph = [ [ ' ' for _ in range(20) ] for _ in range(10) ]

col = 0
for x in num:
    for row in range(9, 9-x//10, -1):
        graph[row][col] = '#'
    col+=2

for row in range(10):
    for col in range(20):
        print(graph[row][col], end='')
    print()