glob = []


def parrot(phrase):
    if phrase in glob:
        print(phrase)
    else:
        glob.append(phrase)

