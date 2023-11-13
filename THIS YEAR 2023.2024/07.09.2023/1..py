class Note:
    def __init__(self, abc, *args):

        if not args:
            self.notes = abc
            self.cba = False
        else:
            self.notes = abc
            self.cba = args[0]

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


do_1 = Note("до", False)
doo = Note("до", True)
do_2 = Note("до")
print(do_1, doo, do_2)
