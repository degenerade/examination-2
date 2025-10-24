"""Abstract intelligence base class and protocol for player strategies."""

from abc import ABC, abstractmethod


class Intelligence(ABC):
    """
    Abstract base class for all intelligence behaviours.
    Any subclass must implement decide_action().
    """

    @abstractmethod
    def decide_action(self, player, game, dicehand):
        """
        Decide whether to roll or hold.
        Must return a string like 'r' (roll) or 'h' (hold).
        """
        pass
