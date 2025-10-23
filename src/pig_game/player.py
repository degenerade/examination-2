"""player for Pig game"""

from typing import Optional

class Player:
    
    def __init__(self, name: str, is_ai: bool = False):
        self.name = name
        self.total_score = 0
        self.turn_score = 0
        self.is_ai = is_ai
        """just declaring vars"""

    def add_turn_points(self, pts: int) -> None:
        self.turn_score += pts
        """we add points to the current turn"""

    def bank_turn(self) -> None:
        self.total_score += self.turn_score
        self.turn_score = 0
        """we move turn_score into total_score and reset turn_score"""

    def lose_turn(self) -> None:
        self.turn_score = 0
        """we lose the current turn's points"""

    def reset(self) -> None:
        self.total_score = 0
        self.turn_score = 0
        """we reset all scores"""

    def __repr__(self):
        return f"Player(name={self.name!r}, total={self.total_score}, turn={self.turn_score}, ai={self.is_ai})"
    