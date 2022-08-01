n = int(input( ))
data = list(map(int, input( ).split( )))
m = int(input( ))
questions = list(map(int, input( ).split( )))
for q in questions:
     start = 0
     end = n - 1
     while start <= end:
         mid = (start + end) // 2
         if data[mid] < q:
               start = mid + 1
         elif data[mid] > q:
               end = mid - 1
         else:
               print("%d "%(mid + 1), end = '')
               break
              
     if start > end:
         print("-1 ", end = ' ')
