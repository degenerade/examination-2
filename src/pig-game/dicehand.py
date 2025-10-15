
import dice


class DiceHand:

    roll_total = 0

    def __init__(self):
        self.previous_roll = 0

    def get_roll(self, die: dice.Dice):
        roll = die.roll_die()
        self.previous_roll = roll
        self.roll_total = roll
        return roll
