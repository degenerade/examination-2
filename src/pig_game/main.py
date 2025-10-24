from .game_setup import GameSetup
from .game import Game
from .highscore import HighScore


class Main:

    @staticmethod
    def run():
        try:
            setup = GameSetup()
            players = setup.create_players()
            dice_hand = setup.create_dice_hand()

            highscore = HighScore()
            game = Game(players, dice_hand, highscore=highscore)
            game.play()
        except (KeyboardInterrupt, EOFError):
            print("\nGame interrupted. Thanks for playing!")
        except (ValueError, TypeError) as exc:
            print(f"\nConfiguration error: {exc}")


if __name__ == "__main__":
    Main.run()
