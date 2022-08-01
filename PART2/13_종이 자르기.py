n, m = map(int, input( ).split( ))
for row in range(1, m + 1):
    for col in range(1, n + 1):
       if row == 1 or row == m:
           if col == 1 or col == n:
                print('+', end = '')
           else:
                print('-', end = '')
       elif col == 1 or col == n:
            print('|', end = '')
       else:
            print(' ', end = '')
    print( )
