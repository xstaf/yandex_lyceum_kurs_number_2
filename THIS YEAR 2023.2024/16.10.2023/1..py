import csv
from sys import stdin

for line in stdin:
    abc = (line.rstrip("\n"))
abc = abc.split(' ')
first = int(abc[0])
second = int(abc[1])
data = []
id_host = []
with open('flatterers.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    for index, row in enumerate(reader):
        if index != 0:
            if abs(int(row[2])) >= first and abs(int(row[3])) >= second:
                id_host.append(data[1] + ' (' + data[0] + ')')
for i in range(len(id_host)):
    print(id_host[i])
