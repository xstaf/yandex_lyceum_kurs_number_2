while True:
    name = input()
    if name.capitalize() and name[1:].islower() and name.isalpha():
        sp_name = name.split()
        if len(sp_name) == 1:
            print(name)
            break