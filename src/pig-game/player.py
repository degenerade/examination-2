from typing import Optional

class Player:
    
    def __init__(self, name: str, is_ai: bool = False):
        self.name = name
        self.total_score = 0
        self.turn_score = 0
        self.is_ai = is_ai

    def add_turn_points(self, pts: int) -> None:
        self.turn_score += pts

    def bank_turn(self) -> None:
        self.total_score += self.turn_score
        self.turn_score = 0

    def lose_turn(self) -> None:
        self.turn_score = 0

    def reset(self) -> None:
        self.total_score = 0
        self.turn_score = 0

    def __repr__(self):
        return f"Player(name={self.name!r}, total={self.total_score}, turn={self.turn_score}, ai={self.is_ai})"
    