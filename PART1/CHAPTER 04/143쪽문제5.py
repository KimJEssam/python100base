n = int(input("학생의 수를 입력하세요 : "))
a = [0]*n
mx = 0
for i in range(n):
    a[i] = int(input("%d번 학생의 성적을 입력하세요." % (i+1)))
    if mx < a[i]:
        mx = a[i]
print("최고 점수는 %d점 입니다." % mx)
