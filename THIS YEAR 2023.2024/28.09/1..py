import random

f = open("lines.txt", encoding="utf8")
lines = f.readlines()
if lines:
    print(lines[random.randrange(len(lines))])
