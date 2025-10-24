
from .dice import Dice
from .utils.histogram import Histogram


class DiceHand:

    def __init__(self, dice_list=None, histogram=None):
        if dice_list is None:
            dice_list = [Dice()]
        if not isinstance(dice_list, (list, tuple)):
            raise TypeError("dice_list must be a sequence of Dice objects.")
        self.dice = []
        for die in dice_list:
            if not isinstance(die, Dice):
                raise TypeError("Every item in dice_list must be a Dice instance.")
            self.dice.append(die)
        self.previous_roll = []
        self.history = []
        self.histogram = histogram or Histogram()

    def get_roll(self):
        if not self.dice:
            raise ValueError("Cannot roll an empty dice hand.")
        self.previous_roll = [die.roll_die() for die in self.dice]
        total = sum(self.previous_roll)
        self.history.append(self.previous_roll.copy())
        self.histogram.add(total)
        return total
            

    def reset_history(self):
        self.history.clear()
