from .dice import Dice


class DiceHand:
    """Wraps one or more dice. Original code uses a single die, so provide roll_one()."""
    def __init__(self, count: int = 1, sides: int = 6):
        assert count >= 1
        self.dice = [Dice(sides) for _ in range(count)]


def roll_one(self) -> int:
    return self.dice[0].roll()