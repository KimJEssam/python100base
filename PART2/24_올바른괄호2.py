s=input()
stack=[]

for x in s:
    if x == '(':
        stack.append(x)
    else:
        if stack == []:
            print("bad")
            exit()
        stack.pop()

if stack == []:
    print("good")
else:
    print("bad")
