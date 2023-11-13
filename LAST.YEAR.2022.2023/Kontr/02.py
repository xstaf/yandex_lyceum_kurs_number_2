def roads(*lines):
    slovar = {'short': [],
              'long': [],
              'very long': [],
              'wonderful': []}
    for line in lines:  # перебор слов из передонного массива
        count_of_caps = 0
        for letter in line:  # по буквам
            if letter.isupper():  # если буквы капсом + 1
                count_of_caps += 1
            if count_of_caps >= 2:
                slovar['wonderful'].append(line)
            if len(line) <= 10:
                slovar['short'].append(line)
            elif len(line) <= 25 and len(line) > 10:
                slovar['long'].append(line)
            if len(line) > 25:
                slovar['very long'].append(line)
    slovar['short'].sort()
    slovar['long'].sort()
    slovar['very long'].sort()
    slovar['wonderful'].sort()

    return slovar


data = [
    'road through the Forest',
    'road along the bank of a Clear ,'
    'stream',
    'In the Clouds',
    'on the field',
    'under the Magic Oak Tree'
]
print(roads(*data))
