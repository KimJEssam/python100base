n = int(input())
setn = set(map(int, input().split()))    #집합 자료구조
m = int(input())
setm = set(map(int, input().split()))    #집합 자료구조

s1 = setn & setm     #교집합 연산
s2 = setn | setm      #합집합 연산

if s1==set():           #공집합이면
    print(0, end='')
for x in sorted(s1):
    print("%d "%x, end='')
print()
for x in sorted(s2):
    print("%d "%x, end='')