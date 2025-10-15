from dicehand import DiceHand
from player import Player

class Game:
    """
    Encapsulates the game flow from the original script:
    - ask for number of players (1-4)
    - loop turns until a player's score reaches 100
    - on a player's turn, prompt for rolling (y/n)
    - rolling a 1 causes turn total to be lost
    - otherwise accumulate turn total and add to player's score when they hold
    """
    def __init__(self, dicehand: DiceHand, max_score: int = 100):
        self.dicehand = dicehand
        self.max_score = max_score
        self.players = []

    def choose_players(self):
        """Ask user for number of players (1-4) and create Player objects."""
        while True:
            players = input("Enter the number of players (1-4): ")
            if players.isdigit():
                players = int(players)
            if 1 <= players <= 4:
                break
            print("Invalid input. Please enter a number between 1 and 4.")
        self.players = [Player(i + 1) for i in range(players)]

    def run(self):
        """Run the main game loop, following the original script logic."""
        # retain the original script's single initial roll call (value = roll())
        # (it has no effect on gameplay but it existed in the original)
        value = self.dicehand.roll_one()


        # Play until some player reaches max_score
        while max(p.score for p in self.players) < self.max_score:
            for player in self.players:
                print(f"\nPlayer {player.index} 's turn.")
                print("Your current score is", player.score, "\n")


                current_score = 0


                while True:
                    should_roll = input("Do you want to roll (y/n)? ")
                    if should_roll.lower() != "y":
                        break
                    value = self.dicehand.roll_one()
                    if value == 1:
                        print("You rolled a 1! No points this turn.")
                        current_score = 0
                        break
                    else:
                        current_score += value
                        print(f"You rolled a {value}.")


                    print(f"Your current score is {current_score}.")


                player.score += current_score
                print(f"Player {player.index}'s total score is {player.score}.")


                # check for end condition to avoid extra turns after someone wins
                if max(p.score for p in self.players) >= self.max_score:
                    break


        # determine winner (first max index as in original)
        max_score_val = max(p.score for p in self.players)
        player_winner_index = next(i for i, p in enumerate(self.players) if p.score == max_score_val)
        print(f"\nPlayer {self.players[player_winner_index].index} wins with a score of {max_score_val}!")