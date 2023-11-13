from sys import stdin

files = []
text = []
for line in stdin:
    files.append(line.rstrip("\n"))
for fname in files:
    f = open(fname, mode='r')
    summi = []
    for line in f.readlines():
        a = line.split()
        a = list(map(int, a))
        summi.append(sum(a))
    avg = (min(summi) + max(summi)) / 2
    round(avg, 1)
    text.append(str(f'For {fname} check is {avg}'))
    print(text)
    f.close()
txt = '\n'.join(text)
print()
a = open('house.txt', mode='w')
a.write(txt)
a.close()
