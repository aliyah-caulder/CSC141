# Imports the random library to represent a die using a class. Rolls the die 10 times.

import random

class Die:
    """A simple attempt to represent a die."""

    def __init__(self, sides=6):
        """Initalize attributes of a die."""
        self.sides = sides

    def roll_die(self):
        """Roll the die and get a number."""
        result = random.randint(1, self.sides)
        print(result)

die = Die(6)

for i in range(1, 11):
    die.roll_die()