import random


def make_bingo():
    a = list()

    schot = 0
    schot1 = 5
    rnd = random.sample(range(1, 75 + 1), 24)
    r = rnd[:12] + [0] + rnd[12:]
    for i in range(5):
        a.append(r[schot:schot1:])
        schot += 5
        schot1 += 5
    print(a)





res = make_bingo()
