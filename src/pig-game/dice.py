"""dice module, contains the Dice class"""
import random


class Dice:
    """Dice class, contains roll_die, set_sides, get_rolls_made,
    get_sum_of_all_rolls"""
    sides = 6

    def __init__(self):
        """Initialize dice object"""
        random.seed()
        self.rolls_made = 0
        self.sum_of_all_rolls = 0

    def set_sides(self, sides):
        """Set the amount of sides the dice will have"""
        self.sides = sides
        print(f"Number of sides set to {sides}")

    def roll_die(self):
        """Roll the dice once and return the value"""
        self.rolls_made += 1
        roll = random.randint(1, self.sides)
        self.sum_of_all_rolls += roll
        return roll

    def get_rolls_made(self):
        """Return the total amount of rolls the dice has made"""
        return self.rolls_made

    def get_sum_of_all_rolls(self):
        """Return the sum of all rolls"""
        return self.sum_of_all_rolls
