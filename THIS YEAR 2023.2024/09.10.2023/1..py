f = open('evening.txt', mode='r')
a = open('summer_eve.txt', mode='w')
data = f.read().lower().split('\n')
omg = []
tmp = []
for i in range(len(data)):
    tmp2 = ''
    if data[i].count(' ') >= 2:
        tmp = data[i].split()
        tmp = tmp[:3]
        tmp2 = ' '.join(tmp).capitalize()
        if tmp2 not in omg:
            omg.append(tmp2)
omg = '\n'.join(omg)
a.write(omg)
f.close()
a.close()
