def reverse():
    f = open('input.dat', mode='rb')
    a = open('output.dat', mode='w+')
    a.close()
    a = open('output.dat', mode='wb')
    data = f.read()
    a.write(data[::-1])
    f.close()
    a.close()


reverse()
