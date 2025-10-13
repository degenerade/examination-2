
import dice


class DiceHand:

    def __init__(self):
        self.previous_roll = 0

    def get_roll(self, die: dice.Dice):
        roll = die.roll_die()
        self.previous_roll = roll
        return roll
