alphabet = input()
number = int(input())
if number >= 0:
    while number > len(alphabet):
        number -= len(alphabet)
    print(alphabet[number:] + alphabet[0:number])
    print(alphabet)
    print(alphabet[len(alphabet) - number:len(alphabet)] + alphabet[:len(alphabet) - number])
elif number < 0:
    number = -number
    while number > len(alphabet):
        number -= len(alphabet)
    print(alphabet[len(alphabet) - number:len(alphabet)] + alphabet[:len(alphabet) - number])
    print(alphabet)
    print(alphabet[number:len(alphabet)] + alphabet[0:number])

