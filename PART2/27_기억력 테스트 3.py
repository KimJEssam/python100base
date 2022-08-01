def binary_search(start, end, q):
     mid = (start + end) // 2
     if start > end:
         return -1
     if data[mid] < q:
         return binary_search(mid + 1, end, q)
     elif data[mid] > q:
         return binary_search(start, mid - 1, q)
     else:
         return mid + 1
        
n = int(input( ))
data = list(map(int, input( ).split( )))
m = int(input( ))
questions = list(map(int, input( ).split( )))
for q in questions:
     print("%d "%(binary_search(0, n - 1, q)), end = ' ')
