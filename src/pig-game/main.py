from dicehand import DiceHand
from game import Game


class Main:
    """Entry point to construct game and start it."""
    @staticmethod
    def run():
        dicehand = DiceHand(count=1, sides=6)
        game = Game(dicehand=dicehand, max_score=100)
        game.choose_players()
        game.run()




if __name__ == "__main__":
    Main.run()
