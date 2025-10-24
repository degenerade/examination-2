from .intelligence import Intelligence


class HumanIntelligence(Intelligence):
    """Handles input from human player"""

    def decide_action(self, player, game, dicehand):
        while True:
            choice = input(f"{player.name}, Roll, Hold, or Quit? (r/h/q):\n>>> ").lower()
            if choice in ["r", "h", "q", "+"]:
                return choice
            print("ERM..... 'r' or 'h' ONLY ???? Is that so hard? Try again...")
