first = 0
second = 0
third = 0
firth = 0

turt = []
n = int(input())
for i in range(n):
    coor = input().split()
    a = coor[0]
    b = coor[1]
    turt.append((a, b))
for i in range(n):
    if '0' in turt[i]:
        a = int(turt[i][0])
        b = int(turt[i][1])
        print((a, b))

for i in range(n):
    a = int(turt[i][0])
    b = int(turt[i][1])
    if a > 0 and b > 0:
        first += 1
    elif a > 0 and b < 0:
        firth += 1
    elif a < 0 and b > 0:
        second += 1
    elif a < 0 and b < 0:
        third += 1

print('I: ' + str(first) + ', II: ' + str(second) + ', III: ' + str(third) + ', IV: ' + str(firth) + '.')
