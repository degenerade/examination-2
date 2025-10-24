"""Medium-difficulty AI using a simple heuristic to decide actions."""

from .intelligence import Intelligence
from ..game import Game
from ..player import Player


class MediumIntelligence(Intelligence):
    """this class allows for better Pig play."""

    def decide_action(self, player: Player, game: Game, dicehand):
        """Decide whether to roll or hold using a simple heuristic.

        Returns 'r' to roll or 'h' to hold.
        """
        opponents = [p for p in game.players if p != player]
        highest_opponent_score = max((p.total_score for p in opponents), default=0)

        remain = game.WINNING_SCORE - player.total_score

        if player.total_score + player.turn_score >= game.WINNING_SCORE:
            return "h"

        # so, if you're ahead, play safer; if behind, push harder
        lead_factor = (player.total_score - highest_opponent_score) / game.WINNING_SCORE
        risk_tolerance = 0.2 - lead_factor * 0.15

        # this is an optimal hold threshold
        threshold = max(10, min(25, remain / (4 + risk_tolerance * 2)))

        if player.turn_score < threshold:
            return "r"
        else:
            return "h"
