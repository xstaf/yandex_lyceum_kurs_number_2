class globa:
    def __init__(self):
        pass
    def __str__(self):
        if self.cba:
            if self.notes == 'до':
                return 'до-о'
            elif self.notes == 'ре':
                return 'ре-э'
            elif self.notes == 'ми':
                return 'ми-и'
            elif self.notes == 'фа':
                return 'фа-а'
            elif self.notes == 'соль':
                return 'со-оль'
            elif self.notes == 'ля':
                return 'ля-а'
            elif self.notes == 'си':
                return 'си-и'
        else:
            return self.notes

    def is_long:
        pass

    def PITCHES(self):
        return ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note(globa):
    pass


class LoudNote(globa):
    pass


class DefaultNote(globa):
    pass


class NoteWithOctave(globa):
    pass


print(Note("соль"))

print(LoudNote(PITCHES[4]))
print(LoudNote("си", is_long=True))

print(DefaultNote("ми"))
print(DefaultNote())
print(DefaultNote(is_long=True))

print(NoteWithOctave("ре", "первая октава"))
print(NoteWithOctave("ля", "малая октава", is_long=True))
