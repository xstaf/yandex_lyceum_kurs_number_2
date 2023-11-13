import random

count = int(input())
ingridients = input().strip()
calloria_a, calloria_b = (float(x) for x in input().strip())
ingrid = random.sample(ingridients, count)
for i in range(count):
    name = ingrid[i]
    namder = random.randint(1, 10 + 1)
    content = round(random.uniform(calloria_a, calloria_b), 1)
    time = round((namder * count) / 10, 1)
    print(f'{i + i}.{name} {namder} of pieces, calories {content}kkal, cooking time {time} ')
