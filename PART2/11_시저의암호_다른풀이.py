sentence = input()

enc = "abcdefghijklmnopqrstuvwxyz"
dec = "xyzabcdefghijklmnopqrstuvw"
enc = list(enc)
dec = list(dec)

for c in sentence: 
    if 'a' <= c <= 'z':
        print(dec[enc.index(c)], end='')
    else:
        print(' ', end='')
