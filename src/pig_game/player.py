"""player for Pig game"""

from typing import Optional


class Player:
    def __init__(self, name: str, is_ai: bool = False, intelligence=None):
        """just declaring vars"""
        self.name = name
        self.total_score = 0
        self.turn_score = 0
        self.is_ai = is_ai
        self.intelligence = intelligence

    def add_turn_points(self, pts: int) -> None:
        """we add points to the current turn"""
        self.turn_score += pts

    def bank_turn(self) -> None:
        """we move turn_score into total_score and reset turn_score"""
        self.total_score += self.turn_score
        self.turn_score = 0

    def lose_turn(self) -> None:
        """we lose the current turn's points"""
        self.turn_score = 0

    def reset(self) -> None:
        """we reset all scores"""
        self.total_score = 0
        self.turn_score = 0

    def __repr__(self):
        return f"Player(name={self.name!r}, total={self.total_score}, turn={self.turn_score}, ai={self.is_ai})"
