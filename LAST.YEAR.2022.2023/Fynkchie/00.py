def space_game(text):
    col_vo_probelov = 0
    for i in text:
        if i == ' ':
            col_vo_probelov += 1
    if col_vo_probelov % 2 == 0:
        print('Вы выиграли')
    else:
        print('Вы проиграли')


space_game('a b c   d')