from dice import Dice
from dicehand import DiceHand
from player import Player
from intelligence.intelligence_human import HumanIntelligence
from intelligence.intelligence_basic import BasicIntelligence

class GameSetup:
    """Handles user input and game initialization."""
    
    def __init__(self):
        self.players = []
        self.dice_hand = None

    def create_players(self):
        """Prompt user for player info and reutn a list of player objects."""
        num_players = int(input("How many players?\n>>> "))
        
        for i in range(num_players):
            name = input(f"Enter name for player {i + 1}\n>>> ")
            is_ai = input(f"Is {name} the computer? (y/n)\n>>> ").lower() == 'y'
            
            if is_ai:
                diff = input("Select difficulty (basic)\n>>> ").lower()
                if diff == 'basic':
                    intelligence = BasicIntelligence()
            else:
                intelligence = HumanIntelligence()
            
            player = Player(name, is_ai=is_ai, intelligence=intelligence)
            self.players.append(player)
        
        return self.players

    def create_dice_hand(self):
        """prompt user for dice configuration"""
        num_dice = int(input("How many dice in play?\n>>> "))
        dice_list=[]
        
        for i in range(num_dice):
            sides = int(input(f"How many sides for die {i + 1}?\n>>> "))
            dice_list.append(Dice(sides))
        
        self.dice_hand = DiceHand(dice_list)
        return self.dice_hand
