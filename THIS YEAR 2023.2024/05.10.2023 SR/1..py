f = open('../09.10.2023/fat.txt', mode='r')
a = open('../09.10.2023/evening.txt', mode='w')
data = f.read().lower().split('\n')
omg = []
tmp = []
for i in range(len(data)):
    tmp2 = ''
    if data[i].count(' ') <= 1:
        tmp = data[i].split()
        for k in range(len(tmp)):
            if len(tmp) == 1:
                tmp2 = tmp[-1 + k]
            else:
                tmp2 = tmp[-1] + ' ' + tmp[-2]
        if tmp2 not in omg:
            omg.append(tmp2)
omg = ', '.join(omg)
a.write(omg)
f.close()
a.close()
