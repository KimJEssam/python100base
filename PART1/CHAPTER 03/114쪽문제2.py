score1 = int(input("과목1의 점수를 입력하세요 : "))
score2 = int(input("과목2의 점수를 입력하세요 : "))
if( score1 >= 60 ):
    if( score2 >= 60 ):
        print("합격")
    else:
        print("불합격")
else:
    print("불합격")