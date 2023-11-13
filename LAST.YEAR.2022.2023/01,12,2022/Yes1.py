one = input().split()
tptheer = input().split()
thring = input().split()
a = set(one + tptheer + thring)
a = list(a)
print('+'.join(a))
a.sort()
okjmn = a[0]
for word in okjmn:
    if len(a) > len(okjmn):
        okjmn = word
    elif len(word) == len(okjmn):
        okjmn = word
print(okjmn)
