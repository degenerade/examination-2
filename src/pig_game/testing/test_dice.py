"""Unit testing for Dice class"""

import unittest
from pig_game.dice import Dice


class TestDice(unittest.TestCase):
    """Test the Dice class"""

    def testInitDefaultObject(self):
        """Instantiate a dice object and test its properties"""
        die = Dice()
        self.assertIsInstance(die, Dice)

        res = die.sides
        exp = 6
        self.assertEqual(res, exp)

    def test_roll_die(self):
        """Roll a dice and check its value is in bounds"""
        die = Dice()

        res = die.roll_die()
        exp = 1 <= res <= die.sides
        self.assertTrue(exp)


if __name__ == "__main__":
    unittest.main()
