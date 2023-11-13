import sys
data = list(map(str.strip, sys.stdin))
data2 = []
for i in data:
    q = 0
    w
    for j in i:
        q += 1
    if len(i) > j:
        line = i.split()[:3]
    else:
        j += len(i)
    data2.append(" ".join(line))
data2.sort(reverse=True)
for i in data2:
    print(i)