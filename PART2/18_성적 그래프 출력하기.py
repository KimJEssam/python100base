num = list(map(int, input( ).split( )))
graph = ['  ' * 20] * 10

col = 0
for x in num:
    for row in range(9, 9-x//10, -1):
         graph[row] = graph[row][:col] + '#' + graph[row][col + 1:]
    col += 2
for row in range(10):
    print(graph[row])
