class Hanger:
    def __init__(self, name, time, oddness=0):
        self.name = str(name)
        self.time = int(time)
        self.oddness = oddness

    def time_inc(self, other):
        self.time += other
        self.oddness += other // 2

    def __add__(self, other):
        hg_new_name = self.name[1] + other.name[-1]
        other.hg_new = 0
        return Hanger(hg_new_name, time=0, oddness=12)

    def __imod__(self, y):
        self.oddness = self.oddness % y

    def __str__(self):
        return f'Hanger by name {self.name} ({self.time}, {self.oddness}>)'

    def __lt__(self, other):  # x < y
        if self.oddness < other.oddness:
            return True
        if self.time < other.time:
            return True
        if self.name > other.name:
            return True
        return False

    def __le__(self, other):  # x ≤ y
        if self.oddness <= other.oddness:
            return True
        if self.time <= other.time:
            return True
        if self.name >= other.name:
            return True
        return False

    def __eq__(self, other):  # x == y
        if self.oddness == other.oddness:
            return True
        if self.time == other.time:
            return True
        if self.name == other.name:
            return True
        return False

    def __gt__(self, other):  # x > y
        if self.oddness > other.oddness:
            return True
        if self.time > other.time:
            return True
        if self.name < other.name:
            return True
        return False

    def __ge__(self, other):  # x ≥ y
        if self.oddness >= other.oddness:
            return True
        if self.time >= other.time:
            return True
        if self.name >= other.name:
            return True
        return False

    def __ne__(self, other):  # x != y
        if self.oddness != other.oddness:
            return True
        if self.time != other.time:
            return True
        if self.name != other.name:
            return True
        return False

    def __repr__(self):
        return self.time * self.oddness


hg = Hanger('Rual Illmarrannen', 3)
hg1 = Hanger('Lart Marran', 1, 5)
hg2 = hg + hg1
print(hg > hg1, hg <= hg2, hg != hg1, sep='\n')
print(hg, hg1, hg2, sep='\n')
hg2.time_inc(3)
id_hg1 = id(hg1)
hg1 %= 4
print(hg < hg2, hg == hg2, hg1 >= hg2, sep='\n')
print(hg, hg1, hg2, sep='\n')
print(id_hg1 == id(hg1))
