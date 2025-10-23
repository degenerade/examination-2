from game_setup import GameSetup
from game import Game

class Main:

    @staticmethod
    def run():
        setup = GameSetup()
        players = setup.create_players()
        dice_hand = setup.create_dice_hand()
        
        game = Game(players, dice_hand)
        game.play()
        

if __name__ == '__main__':
    Main.run()