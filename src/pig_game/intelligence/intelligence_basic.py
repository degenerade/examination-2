import random
from intelligence import Intelligence

class BasicIntelligence(Intelligence):
    """Fully random, mainly for testing"""
    
    def decide_action(self, player, game, dicehand):
        return random.choice(['r', 'h'])
