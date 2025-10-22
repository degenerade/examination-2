"""intelligence thinking for Pig; needs review"""

from typing import Protocol


class Strategy(Protocol):
    def should_roll(self, player_total: int, player_turn_score: int, opponent_total: int, goal: int) -> bool:
        ...


class SmartHeuristicStrategy:

    """this class allows for better Pig play."""

    def should_roll(self, player_total: int, player_turn_score: int, opponent_total: int, goal: int) -> bool:
        #leftover points to win
        remain = goal - player_total

        if player_total + player_turn_score >= goal:
            return False

        #so, if you're ahead, play safer; if behind, push harder
        lead_factor = (player_total - opponent_total) / goal
        risk_tolerance = 0.2 - lead_factor * 0.15

        #this is an optimal hold threshold
        threshold = max(10, min(25, remain / (4 + risk_tolerance * 2)))

        return player_turn_score < threshold


#for now, this class is for compatibility.

class ThresholdStrategy:
    def __init__(self, threshold: int = 20):
        self.threshold = threshold

    def should_roll(self, player_total: int, player_turn_score: int, opponent_total: int, goal: int) -> bool:
        if player_total + player_turn_score >= goal:
            return False
        return player_turn_score < self.threshold


class CautiousStrategy(ThresholdStrategy):
    def __init__(self):
        super().__init__(threshold=10)
