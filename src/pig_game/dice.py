"""dice module, contains the Dice class"""

import random


class Dice:
    """Dice class, contains roll_die, set_sides, get_rolls_made,
    get_sum_of_all_rolls"""

    def __init__(self, sides: int = 6):
        """Initialize dice object"""
        random.seed()
        self.sides = sides

    def roll_die(self):
        """Roll the dice once and return the value"""
        roll = random.randint(1, self.sides)
        return roll
