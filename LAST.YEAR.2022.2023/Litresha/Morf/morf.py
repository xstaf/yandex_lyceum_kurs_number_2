import pymorphy2
import sys

coin = 0
morph = pymorphy2.MorphAnalyzer()
a = sys.stdin.read().lower()
simvol = 'йцукенгшщзхъфывапролджэячсмитьбю \n'
text = ''
slochit = []
otvet = []
for s in a:
    if s in simvol:
        text += s
for text in text.split():
    info = morph.parse(text)[0]
    if info.tag.POS == 'NOUN' and info.score > 0.5:
        slochit.append(info.normal_form)
for i in slochit:
    if slochit.count(i) == 1:
        otvet.append(i)
print(*otvet)



