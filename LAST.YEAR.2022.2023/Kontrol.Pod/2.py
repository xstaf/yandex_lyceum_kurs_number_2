whaite = []
blake = []
raimboy = []
for i in range(int(input())):
    chisla = int(input())
    if chisla > 40 and chisla < 120:
        whaite.append(chisla)
    elif chisla > 120 and chisla % 6 == 0:
        blake.append(chisla)
    elif chisla < 40:
        raimboy.append(chisla)
print('(White Pointed mushrooms)_', max(whaite))
print('(Black Blunt-pointed mushrooms)_', max(blake) * min(blake))
print('(Rainbow mushrooms)_', sum(raimboy))