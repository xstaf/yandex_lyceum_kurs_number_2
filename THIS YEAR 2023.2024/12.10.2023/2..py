import csv

word = ''
data = []
minim = []
minimTMP = []
with open('wares.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for index, row in enumerate(reader):
        data.append([row[0], row[1]])
        minimTMP.append(int(row[1]))
    minim = int(min(minimTMP))
    minimTMP.pop(minim)
    summ = 1000
    while minim <= summ:
        for i in range(len(data)):
            if word.count(data[i][0]) >
            if minim == int(data[i][1]):
                if word == '':
                    word = data[i][0]
                    summ -= minim

                else:
                    word = word + ', ' + data[i][0]

                break
    if word == '':
        print('error')
    print(word)
