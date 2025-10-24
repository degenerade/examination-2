"""dice module, contains the Dice class"""

import random


class Dice:
    """Dice class, contains roll_die, set_sides, get_rolls_made,
    get_sum_of_all_rolls"""

    def __init__(self, sides: int = 6):
        """Initialize dice object"""
        self._validate_sides(sides)
        random.seed()
        self.sides = sides

    def roll_die(self):
        """Roll the dice once and return the value"""
        roll = random.randint(1, self.sides)
        return roll

    @staticmethod
    def _validate_sides(sides: int) -> None:
        if not isinstance(sides, int):
            raise TypeError("Number of sides must be an integer.")
        if sides < 2:
            raise ValueError("A die must have at least two sides.")

    def set_sides(self, sides: int) -> None:
        """Update the number of sides on the die."""
        self._validate_sides(sides)
        self.sides = sides
