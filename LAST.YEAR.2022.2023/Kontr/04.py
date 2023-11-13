class GreatMagician:
    def __init__(self, name, *spels, power=10):
        self.name = name
        self.spels = list(spels)
        self.power = power

    def add(self, newspel):
        self.spels.insert(0, newspel)
        self.power + len(newspel) // 2

    def __str__(self):
        spel = ', '.join(self.spels)
        return f'GreatMagician by name {self.name} {spel},{self.power}'

    def __call__(self, value):
        coin = 0
        for spell in self.spels:
            if len(spell) > value:
                coin += 1
        return coin

    def __add__(self, other):
        new = self.name[:3] + other.name[:3]
        spells1 = set(self.spels)
        spells2 = set(other.spels)
        new_spels = list(spells1.intersection(spells2))
        new_spels.sort()
        return GreatMagician(new, *new_spels)

    def __sub__(self, spell):
        if spell in self.spels:
            self.spels.remove(spell)
            print(f'Delete{spell}')
        else:
            print('Nothing to delete')

    def __lt__(self, other):  # x < y
        if self.power < other.power:
            return True
        if len(self.spels) < len(other.spels):
            return True
        if self.name > other.name:
            return True
        return False

    def __le__(self, other):  # x ≤ y
        if self.power <= other.power:
            return True
        if len(self.spels) <= len(other.spels):
            return True
        if self.name >= other.name:
            return True
        return False

    def __eq__(self, other):  # x == y
        if self.power == other:
            return True
        if len(self.spels) == len(other.spels):
            return True
        if self.name == other.name:
            return True
        return False

    def __gt__(self, other):  # x > y
        if self.power > other.power:
            return True
        if len(self.spels) > len(other.spels):
            return True
        if self.name < other.name:
            return True
        return False

    def __ge__(self, other):  # x ≥ y
        if self.power >= other.power:
            return True
        if len(self.spels) >= len(other.spels):
            return True
        if self.name >= other.name:
            return True
        return False

    def __ne__(self, other):  # x != y
        if self.power != other.power:
            return True
        if len(self.spels) != len(other.spels):
            return True
        if self.name != other.name:
            return True
        return False


gm = GreatMagician('Knuth')
gm1 = GreatMagician('Sam', 'Abracadabra',
                    'Sezam', power=3)
gm.add('Good day')
gm.add('Sezam')
print(gm, gm1, sep='\n')
print(gm < gm1, gm >= gm1, gm != gm1)
gm2 = gm + gm1
print(gm2)
print(gm2 > gm1, gm2 <= gm, gm2 == gm)
