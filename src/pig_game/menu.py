"""Module containing the menu class"""
from .game import Game
from .game_setup import GameSetup
from .highscore import HighScore
from .rules import RULES_TEXT

class Menu:
    """class that will loop the menu"""
    
    def __init__(self):
        self.setup = GameSetup()
        self.highscore = HighScore()
        self.players = None
        self.dice_hand = None
        self.running = True

    def print_menu(self):
        """Print menu options"""
        print("""---------------------------------------
| 1) Play game
| 2) Setup ccustom game (make players and dice)
| 3) Change player names
| 4) Print highscores
| 5) Setup base game (1 player)
| 6) Show rules
| m) Print menu
| q) Quit
 ---------------------------------------""")

    def setup_game(self):
        print("\n--- Setting up game... ---")
        self.players = self.setup.create_players()
        for player in self.players:
            self.highscore.register(player.name)
        self.dice_hand = self.setup.create_dice_hand()
        print("--- Game setup complete. ---\n")
    
    def setup_base_game(self):
        from .player import Player
        from .dice import Dice
        from .dicehand import DiceHand
        from .intelligence.intelligence_human import HumanIntelligence
        from .intelligence.intelligence_basic import BasicIntelligence

        self.players = [Player("Player 1", False, HumanIntelligence())]
        self.dice_hand = DiceHand([Dice(6)])
        for player in self.players:
            self.highscore.register(player.name)

    def change_names(self):
        if not self.players:
            print("You have to create a player first vro 🌹💔...")
            return
        for player in self.players:
            new_name = input(f"""Enter new name for {player.name}:
(Or press enter to keep current)
>>> """)
            if new_name.strip():
                old_name = player.name
                player.name = new_name.strip()
                self.highscore.rename(old_name, player.name)
        print("--- Name updated. ---")

    def show_highscores(self):
        print("--- Hightscores 🏆🏆 ---")
        scores = self.highscore.top(10)
        if not scores:
            print("No highscores recorded yet.")
        else:
            for i, entry in enumerate(scores, start=1):
                games = entry["games_played"]
                avg = entry["total_score"] / games if games else 0
                recent = ", ".join(str(score) for score in entry["scores"][-3:][::-1]) or "-"
                print(
                    f"{i:2d}. {entry['display_name']:15} "
                    f"best: {entry['best_score']:3d} | "
                    f"wins: {entry['wins']:2d}/{games:2d} | "
                    f"avg: {avg:5.1f}"
                )
                print(f"     recent scores: {recent}")

    def show_rules(self):
        print("\n--- Game rules ---")
        print(RULES_TEXT)
    
    def play_game(self):
        if not self.players or not self.dice_hand:
            print("--- Setup the game first lil bro ---")
            return
        print("\n--- 🎮🕹️ starting game. vvvshhhh... ---")
        game = Game(self.players, self.dice_hand, highscore=self.highscore)
        game.play()
    
    def run(self):
        self.print_menu()
        while self.running:
            choice = input("\nEnter your choice:\n>>> ").strip().lower()
            if choice == "1":
                self.play_game()
            elif choice == "2":
                self.setup_game()
            elif choice == "3":
                self.change_names()
            elif choice == "4":
                self.show_highscores()
            elif choice == "5":
                self.setup_base_game()
            elif choice == "6":
                self.show_rules()
            elif choice == "m":
                self.print_menu()
            elif choice == "q":
                print("---> Bye Bye <---")
                self.running = False
            else:
                print("Can u try entering a correct choice??")
                print("Press m to get the menu again")
