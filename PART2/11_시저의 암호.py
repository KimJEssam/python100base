sentence = input( )
for c in sentence:
    if c == 'a':
        print('x', end = '')
    elif c == 'b':
        print('y', end = '')
    elif c == 'c':
        print('z', end = '')
    elif c == ' ':
        print(' ', end = '')
    else:
        print('%c'%chr(ord(c) - 3), end = '')
