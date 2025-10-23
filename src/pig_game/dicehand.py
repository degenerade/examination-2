
from dice import Dice


class DiceHand:

    def __init__(self, dice_list=None):
        if dice_list is None:
            dice_list[Dice()]
        self.dice = dice_list
        self.previous_roll = []
        self.history = []

    def get_roll(self):
        self.previous_roll = [die.roll_die() for die in self.dice]
        self.history.append(self.previous_roll.copy())
        return sum(self.previous_roll)
            

    def reset_history(self):
        self.history.clear()
