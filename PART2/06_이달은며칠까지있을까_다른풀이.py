year, month = input().split()
year = int(year)
month = int(month)

lastday = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year%400 == 0:
    lastday[2] += 1
elif year%4 == 0 and year%100!=0:
    lastday[2] += 1
print(lastday[month])
