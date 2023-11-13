import csv
from sys import stdin

for line in stdin:
    ABC = (line.rstrip("\n"))
ABC = ABC.split(' ')
first = int(ABC[0])
second = int(ABC[1])
itog = []
with open('flatterers.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    for index, row in enumerate(reader):
        print(index, row)

        if index != 0:
            if int(row[i][2]) >= first and int(row[i][3]) >= second:
                if not (row[-1] in things):
                    itog.append(data[i][1] + ' (' + data[i][0] + ')')
for i in itog:
    print(i)
