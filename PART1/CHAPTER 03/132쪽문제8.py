while True:
    n = int(input("수를 입력하시오. : "))
    if n < 0:
        break
    if n == 0:
        continue
    if n%2 == 1:
        print("홀수")
    else:
        print("짝수")
