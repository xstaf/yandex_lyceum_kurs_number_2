import sys
text = sys.stdin.read().split()
text = [i.split('.') for i in text]
enum_spis = enumerate(text)

poftor0 = []
poftor1 = set()

for num, slovo in enum_spis:
    if slovo[0].upper() == "'":
        poftor0.append((num, slovo))
        poftor1.add(slovo)
print(poftor0)
