from .dice import Dice
from .dicehand import DiceHand
from .player import Player
from .intelligence.intelligence_human import HumanIntelligence
from .intelligence.intelligence_basic import BasicIntelligence
from .intelligence.intelligence_medium import MediumIntelligence


class GameSetup:
    """Handles user input and game initialization."""

    def __init__(self):
        self.players = []
        self.dice_hand = None

    def create_players(self):
        """Prompt user for player info and return a list of player objects."""
        num_players = self._input_int("How many players?", min_value=1)

        for i in range(num_players):
            name = self._input_non_empty(f"Enter name for player {i + 1}")
            is_ai = self._input_yes_no(f"Is {name} the computer? (y/n)")

            if is_ai:
                intelligence = self._select_ai_difficulty(name)
            else:
                intelligence = HumanIntelligence()

            player = Player(name, is_ai=is_ai, intelligence=intelligence)
            self.players.append(player)

        return self.players

    def create_dice_hand(self):
        """Prompt user for dice configuration."""
        num_dice = self._input_int("How many dice in play?", min_value=1)
        dice_list = []

        for i in range(num_dice):
            sides = self._input_int(f"How many sides for die {i + 1}?", min_value=2)
            while True:
                try:
                    dice_list.append(Dice(sides))
                    break
                except (TypeError, ValueError) as exc:
                    print(f"Invalid die configuration: {exc}")
                    sides = self._input_int(
                        f"How many sides for die {i + 1}? (minimum 2)",
                        min_value=2,
                    )

        self.dice_hand = DiceHand(dice_list)
        return self.dice_hand

    @staticmethod
    def _input_int(prompt: str, min_value: int = None, max_value: int = None) -> int:
        while True:
            raw = input(f"{prompt}\n>>> ").strip()
            try:
                value = int(raw)
            except ValueError:
                print("Please enter a whole number.")
                continue

            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}.")
                continue
            return value

    @staticmethod
    def _input_non_empty(prompt: str) -> str:
        while True:
            value = input(f"{prompt}\n>>> ").strip()
            if value:
                return value
            print("Please enter a non-empty value.")

    @staticmethod
    def _input_yes_no(prompt: str) -> bool:
        while True:
            value = input(f"{prompt}\n>>> ").strip().lower()
            if value in {"y", "yes"}:
                return True
            if value in {"n", "no"}:
                return False
            print("Please answer with 'y' or 'n'.")

    @staticmethod
    def _select_ai_difficulty(name: str):
        diff = input("Select difficulty ((b)asic/(m)edium)\n>>> ").strip().lower()
        if diff in {"m", "medium"}:
            return MediumIntelligence()
        if diff not in {"b", "basic", ""}:
            print(f"Unknown difficulty '{diff}' for {name}. Defaulting to basic.")
        return BasicIntelligence()
