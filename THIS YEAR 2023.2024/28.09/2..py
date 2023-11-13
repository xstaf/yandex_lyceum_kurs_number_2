alpha = open("cyrillic.txt", encoding="utf8", mode='r')
yep = open('transliteration.txt', encoding='utf8', mode='w')
kirillica = alpha.read()
lis = str(kirillica)
data = []

for a in range(len(lis)):
    data.append(lis[a])

disk = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
        "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
        "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
        "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
        "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
        "б": "b", "ю": "ju", "ё": "jo"}
for i in range(len(data)):
    flag1 = False
    if data[i].lower() in disk:
        if not data[i].lower() == data[i]:
            flag1 = True
        data[i] = disk[data[i].lower()]
        if flag1:
            data[i] = data[i].capitalize()

yep.write(''.join(data))
yep.close()
alpha.close()
