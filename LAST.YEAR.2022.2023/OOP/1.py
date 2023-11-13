class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        if target > self.range:
            return f'Враг слишком далеко для оружия{self.name}'
        if self.range <= target:
            return f'Врагу нанесен урон оружием {self.name} в размере {self.damage}'
