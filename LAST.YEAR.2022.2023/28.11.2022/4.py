a = int(input()[1:])
for i in range(a):
    loij = input()
    if '#' in loij:
        loij = loij[:loij.find('#')]
    loij = loij.rstrip()
    print(loij)

