f1 = open('input.bmp', 'rb').read()
new_data = f1[:54] + bytes([255 - value for value in f1[54:]])


f2 = open('res.bmp', 'wb')
f2.write(new_data)
f2.close()
