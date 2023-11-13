game = ['камень', 'бумага', 'ножницы']
a = input()
b = input()
word = a + b
if a == b:
    print('ничья')
else:
    if 'камень' in word and 'ножницы' in word:
        if a == 'камень':
            print('первый')
        else:
            print('второй')
    if 'камень' in word and 'бумага' in word:
        if a == 'бумага':
            print('первый')
        else:
            print('второй')
    if 'бумага' in word and 'ножницы' in word:
        if a == 'ножницы':
            print('первый')
        else:
            print('второй')
