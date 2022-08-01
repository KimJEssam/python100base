def f(row, col):
    res = sum(mine[row - 1][col - 1 : col + 2])
    res += sum(mine[row][col -1 : col + 2])
    res += sum(mine[row + 1][col - 1 : col + 2])
    return res

mine = [ ]
for row in range(5):
    mine.append([ ])
    mine[row] = list(map(int, input( ).split( )))

maxval = 0
for row in range(1, 4):
    for col in range(1, 4):
       tsum = f(row, col)
       if tsum > maxval:
            maxval = tsum
            
print(maxval)
