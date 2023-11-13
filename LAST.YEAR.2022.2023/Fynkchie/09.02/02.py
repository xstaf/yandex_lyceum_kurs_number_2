
import sys

spisok = []

for i in sys.stdin:
    a = i.split(';')
    spisok.append(a)
for i in spisok:
    coin = 0
    for j in i:
        if len(j) == 2:
            coin += 1
    i.append(coin)

for i in range(len(spisok)):
    for j in range(len(spisok)):
        if i < j:
            spisok.remove(spisok[i])
