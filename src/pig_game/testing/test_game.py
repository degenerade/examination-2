
import unittest
from ..game import Game
from ..player import Player
from ..dicehand import DiceHand
from ..dice import Dice
from ..intelligence.intelligence_human import HumanIntelligence

class TestGameClass(unittest.TestCase):
    
    def setUp(self):
        p1 = Player("BOB", intelligence=HumanIntelligence)
        p2 = Player("MARLEY", intelligence=HumanIntelligence)
        dice = Dice()
        dice_hand = DiceHand([dice])
        self.game = Game([p1, p2], dice_hand)

    def test_switch_turn(self):
        self.assertEqual(self.game.current_player().name, "BOB")
        self.game.switch_turn()
        self.assertEqual(self.game.current_player().name, "MARLEY")

    def test_game_starts_not_over(self):
        self.assertFalse(self.game.game_over)

if __name__ == "__main__":
    unittest.main()