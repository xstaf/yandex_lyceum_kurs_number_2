from sys import stdin

files = []
text = []
for line in stdin:
    files.append(line.rstrip("\n"))
for fname in files:
    f = open(fname, mode='r')
    lines = f.readlines()
    c = 0
    numbers = len(line.split()[0])
    print(lines)
    for line in lines:
        c += 1
        a = line.split()
        a = list(map(int, a))
        if c == 1:
            tmp = []
            for i in range(numbers):
                tmp.append(int(a[i - 1] + a[i]))
            maxim = max(tmp)
        elif c == 3:
            tmp = []
            for i in range(numbers):
                tmp.append(int(a[i - 1] + a[i]))
                minim = min(tmp)
        elif c == 2:
            tmp2 = line
        for i in range(numbers):
            l = int(tmp2[i - 1] + tmp2[i])
            if minim < l < maxim:
                result = l

    text.append(str(f'{fname[0:-4]}({result})'))
    f.close()
txt = '\n'.join(text)
print()
a = open('citizen.txt', mode='w')
a.write(txt)
a.close()
