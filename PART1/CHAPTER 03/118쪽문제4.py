s1, s2, s3 = map(int, input("세 점수를 공백으로 구분하여 입력하세요. : ").split())
if( s1 >= s2 and s1 >= s3 ):
    print(s1)
elif( s2 >= s1 and s2 >= s3 ):
    print(s2)
else:
    print(s3)