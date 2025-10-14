import random


class Dice:
    """Single six-sided die (behaviour from original roll function)."""
    def __init__(self, sides: int = 6):
        self.sides = sides

    def roll(self) -> int:
        """Simulate rolling a die."""
        return random.randint(1, self.sides)