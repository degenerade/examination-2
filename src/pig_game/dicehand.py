
from dice import Dice
from utils.histogram import Histogram


class DiceHand:

    def __init__(self, dice_list=None, histogram=None):
        if dice_list is None:
            dice_list = [Dice()]
        self.dice = dice_list
        self.previous_roll = []
        self.history = []
        self.histogram = histogram or Histogram()

    def get_roll(self):
        self.previous_roll = [die.roll_die() for die in self.dice]
        total = sum(self.previous_roll)
        self.history.append(self.previous_roll.copy())
        self.histogram.add(total)
        return total
            

    def reset_history(self):
        self.history.clear()
