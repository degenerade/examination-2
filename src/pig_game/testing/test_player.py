"""Unit testing for Player class"""


import unittest
from ..player import Player


class TestPlayer(unittest.TestCase):
	def test_init_default(self):
		"""Player initializes with correct default values."""
		p = Player("Alice")
		self.assertIsInstance(p, Player)
		self.assertEqual(p.name, "Alice")
		self.assertEqual(p.total_score, 0)
		self.assertEqual(p.turn_score, 0)
		self.assertFalse(p.is_ai)

	def test_add_and_bank_and_lose(self):
		"""Adding points, banking them, and losing a turn behave correctly."""
		p = Player("Bob")
		p.add_turn_points(5)
		self.assertEqual(p.turn_score, 5)
		p.add_turn_points(3)
		self.assertEqual(p.turn_score, 8)

		p.bank_turn()
		self.assertEqual(p.total_score, 8)
		self.assertEqual(p.turn_score, 0)

		# losing turn should keep total but zero turn
		p.add_turn_points(4)
		p.lose_turn()
		self.assertEqual(p.turn_score, 0)
		self.assertEqual(p.total_score, 8)

	def test_reset_and_repr(self):
		"""Reset clears scores and repr contains the player's name."""
		p = Player("Cara")
		p.add_turn_points(7)
		p.bank_turn()
		self.assertIn("Cara", repr(p))
		p.reset()
		self.assertEqual(p.total_score, 0)
		self.assertEqual(p.turn_score, 0)


if __name__ == "__main__":
	unittest.main()

