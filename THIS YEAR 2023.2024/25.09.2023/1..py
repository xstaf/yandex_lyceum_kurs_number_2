a = ''.join(input().split())
b = str(a)
EndNumber = []
if a.count('--') == 0 and a.count('(') == a.count(')') and a.count('(') + a.count(')') < 3 and a[-1] != '-' and (
        a.count('(') < 0 or not a.find('(') < a.find(')')):
    if a[:1] == '8':
        for i in range(len(b)):
            if b[i].isdigit():
                EndNumber.append(b[i])
        EndNumber = ''.join(EndNumber)
        EndNumber = '+7' + EndNumber[1:]
        if len(EndNumber) == 12:
            print(EndNumber)
        else:
            print('error')
    elif a[:2] == '+7':
        for i in range(len(b)):
            if b[i].isdigit():
                EndNumber.append(b[i])
        EndNumber = ''.join(EndNumber)
        EndNumber = '+' + EndNumber
        if len(EndNumber) == 12:
            print(EndNumber)
        else:
            print('error')
    else:
        print('error')
else:
    print('error')
