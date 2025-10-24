"""Module containing the menu class"""
from .game import Game
from .game_setup import GameSetup
from .highscore import HighScore

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
| m) Print menu
| q) Quit
 ---------------------------------------""")

    def setup_game(self):
        print("\n--- Setting up game... ---")
        self.players = self.setup.create_players()
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

    def change_names(self):
        if not self.players:
            print("You have to create a player first vro 🌹💔...")
            return
        for player in self.players:
            new_name = input(f"""Enter new name for {player.name}:
(Or press enter to keep current)
>>> """)
            if new_name.strip():
                player.name = new_name.strip()
        print("--- Name updated. ---")

    def show_highscores(self):
        print("--- Hightscores 🏆🏆 ---")
        scores = self.highscore.top(10)
        if not scores:
            print("No highscores recorded yet.")
        else:
            for i, (name, score) in enumerate(scores, start=1):
                print(f"{i:2d}. {name:15} {score} pts")
    
    def play_game(self):
        if not self.players or not self.dice_hand:
            print("--- Setup the game first lil bro ---")
            return
        print("\n--- 🎮🕹️ starting game. vvvshhhh... ---")
        game = Game(self.players, self.dice_hand)
        game.play()
        winner = max(game.players, key=lambda p: p.total_score)
        self.highscore.add(winner.name, winner.total_score)
    
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
            elif choice == "m":
                self.print_menu()
            elif choice == "q":
                print("---> Bye Bye <---")
                self.running = False
            else:
                print("Can u try entering a correct choice??")
                print("Press m to get the menu again")