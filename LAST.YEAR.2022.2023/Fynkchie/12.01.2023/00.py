ingredients = [0, 0, 0]


def choose_coffee(*preferencen):
    global ingredients
    for i in preferencen:
        if i == "Эспрессо" and ingredients[0] - 1 >= 0:
            ingredients[0] -= 1
            return i
        elif i == "Капучино" and ingredients[0] - 1 >= 0 and ingredients[1] - 3 >= 0:
            ingredients[0] -= 1
            ingredients[1] -= 3
            return i
        elif i == "Маккиато" and ingredients[0] - 2 >= 0 and ingredients[1] - 1 >= 0:
            ingredients[0] -= 2
            ingredients[1] -= 1
            return i
        elif i == 'Кофе по-венски' and ingredients[0] - 1 >= 0 and ingredients[2] - 2 >= 0:
            ingredients[0] -= 1
            ingredients[2] -= 2
            return i
        elif i == "Латте Маккиато" and ingredients[0] - 1 >= 0 and ingredients[1] - 2 >= 0 and ingredients[2] - 1 >= 0:
            ingredients[0] -= 1
            ingredients[1] -= 2
            ingredients[2] -= 1
            return i
        elif i == 'Кон Панна' and ingredients[0] - 1 >= 0 and ingredients[2] - 1 >= 0:
            ingredients[0] -= 1
            ingredients[2] -= 1
            return i

    return 'К сожалению, не можем предложить Вам напиток'








ingredients = [4, 4, 0]
print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))
print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))
print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))
