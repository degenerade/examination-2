"""DiceHand: roll dice, keep last roll and history."""

from .dice import Dice
from .utils.histogram import Histogram


class DiceHand:
    """Hand of dice for a turn."""

    def __init__(self, dice_list=None, histogram=None):
        """Init with list of Dice or one default."""
        if dice_list is None:
            dice_list = [Dice()]
        self.dice = dice_list
        self.previous_roll = []
        self.history = []
        self.histogram = histogram or Histogram()

    def get_roll(self):
        """Roll all dice; save results, update histogram, return sum."""
        self.previous_roll = [die.roll_die() for die in self.dice]
        total = sum(self.previous_roll)
        self.history.append(self.previous_roll.copy())
        self.histogram.add(total)
        return total

    def reset_history(self):
        """Clear history."""
        self.history.clear()
