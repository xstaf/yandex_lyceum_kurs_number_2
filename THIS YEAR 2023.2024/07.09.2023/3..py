class BellTower:

    def sound(self):
        self.data*()
        print('...')

    def append(self, a):
        self.data.append(a)

    def __init__(self, *args, **kwargs):
        self.data = []
        self.data.append(args)


class LittleBell:
    def __init__(self):
        return self.sound()

    def sound(self):
        print('ding')


class BigBell:

    def __init__(self, *args):
        self.number = 0
        self.words = ['ding', 'dong']
        return self.sound()

    def sound(self):
        print(self.words[self.number % 2])
        self.number += 1


bell_tower = BellTower(BigBell(), LittleBell())
bell_tower.sound()
bell_tower.sound()
bell_tower.append(BigBell())
bell_tower.sound()
bell_tower.sound()
