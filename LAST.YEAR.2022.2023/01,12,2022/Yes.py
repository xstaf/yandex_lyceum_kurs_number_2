o = input()
a = int(input())
o = o.split('#')
pol = []
for i in o:
    if len(i) > 3 and len(i) % a == 0:
        pol.append(i.capitalize())
print(',' .join(pol))
