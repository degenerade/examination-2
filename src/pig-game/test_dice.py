"""Unit testing for Dice class"""

import unittest
import dice


class TestDiceClass(unittest.TestCase):
    """Test the Dice class"""

    def testInitDefaultObject(self):
        """Instantiate a dice object and test its properties"""
        die = dice.Dice()
        self.assertIsInstance(die, dice.Dice)

        res = die.sides
        exp = 6
        self.assertEqual(res, exp)

    def testRollDice(self):
        """Roll a dice and check its value is in bounds"""
        die = dice.Dice()

        res = die.roll_die()
        exp = 1 <= res <= die.sides
        self.assertTrue(exp)


if __name__ == '__main__':
    unittest.main()
