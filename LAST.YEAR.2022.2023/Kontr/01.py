import sys

data = sys.stdin.readlines()
spisok = []

for i in data:
    tmp = i.split()[:3]  # добовляем по 3 слова из стоки
    tmp = tmp[::-1]  # переворачиваем слово , чтобы они небыли в обратном порядке
    spisok.append(' '.join(tmp))  # добовляем итоговую строку в хронилище
spisok.sort(reverse=True)  # отсортируем в обратном порядке
for line in spisok:
    print(line)
