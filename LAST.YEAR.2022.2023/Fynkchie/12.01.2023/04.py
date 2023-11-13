def average(values):
    if len(values) == 0:
        return
    else:
        a = sum(values) / len(values)
        if a == int(a):
            return int(a)
        else:
            return a


print(average([-5, 2]))
