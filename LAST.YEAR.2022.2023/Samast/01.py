import random

ingridients = input().strip().split(', ')
count = int(input())
calories_a, calories_b = (int(x) for x in input().split())

calories = float(input())
ingr = random.sample(ingridients, count)
for i in range(count):
    name = ingr[i]
    numbe = random.uniform(calories_a, calories_b)
    number = int(numbe)

    calorie_value = round(random.uniform(0, calories), 2)
    full_value = round(number * calorie_value, 2)
    print(f'{i + 1}. {name} {number} of pieces, calories {calorie_value} kkal, cooking time {full_value}')
