from random import randint

class Die():
    """pog"""
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)

die_1 = Die(20)
die_1.roll_die()