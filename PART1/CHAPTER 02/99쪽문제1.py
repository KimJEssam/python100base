print("%d" % 10)
print("%s" % "Hello")
a, b = 10, 5
print("%d+%d=%d" % (a, b, a+b))
pi = 3.1415926535
print("%f" % pi)
print("%.1f %.2f %.3f" % (pi, pi, pi))
name = "정보"
print("나의 이름은 %s입니다." % name)
print("나의 이름은 %s입니다." % (name+name))
print("나의 이름은 %s가 아니라 [%10s]입니다." % (name+name, name))
print("나의 이름은 %s가 아니라 [%-10s]입니다." % (name+name, name))