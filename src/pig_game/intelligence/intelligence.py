from abc import ABC, abstractmethod


class Intelligence(ABC):
    """
    Abstract base class for all intelligence behaviours.
    Any subclass must use decide_action().
    """

    @abstractmethod
    def decide_action(self, player, game, dicehand):
        """
        Decide wether to roll or hold.
        Must return string 'r' or 'h'.
        """
        pass
