n = int(input( ))
data = map(int, input( ).split( ))
data = list(data)
maxval = 0
minval = 100
for i in range(n):
    if data[i] > maxval:
        maxval = data[i]
    if data[i] < minval:
       minval = data[i]
print(maxval, minval)
