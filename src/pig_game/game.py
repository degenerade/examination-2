
from player import Player


class Game:
    WINNING_SCORE = 100

    def __init__(self, players, dice_hand):
        self.players = players
        self.dice_hand = dice_hand
        self.current_player_index = 0
        self.game_over = False

    def current_player(self) -> Player:
        """returns the current player object

        Returns:
            Player: current player
        """
        return self.players[self.current_player_index]
    
    def switch_turn(self):
        """Swtich to the other players turn
        """
        self.current_player_index = 1 - self.current_player_index

    def take_turn(self):
        """Single turn for the current player
        """
        player = self.current_player()
        print(f"\n\n--->{player.name}'s turn!")
        
        while True:
            choice = player.intelligence.decide_action(player, self, self.dice_hand)
            
            if choice == 'r':
                roll = self.dice_hand.get_roll()
                print(f"{player.name} rolled {self.dice_hand.previous_roll} (total {roll})")
                
                if 1 in self.dice_hand.previous_roll:
                    print("Uh oh, u rolled a 1 ⚀... No turn for you.")
                    player.lose_turn()
                    break
                else:
                    player.add_turn_points(roll)
                    print(f"Turn total: {player.total_score}")
                    
            elif choice == 'h':
                player.bank_turn()
                print(f"{player.name} banks points. Total score: {player.total_score}")
                break
        
        if player.total_score >= self.WINNING_SCORE:
            print(f"{player.name} wins!!! They won with {player.total_score} points!")
            self.game_over = True
        else:
            self.switch_turn()

    def play(self):
        """main loop to play game
        """
        while not self.game_over:
            self.take_turn()
        self._display_histogram()

    def _display_histogram(self):
        freq = self.dice_hand.histogram.as_freq()
        if not freq:
            print("\nNo rolls recorded.")
            return

        print("\nRoll distribution:")
        for total in sorted(freq):
            share = freq[total]
            bar = "#" * max(1, int(share * 50))
            print(f"{total:>2}: {share:.3f} {bar}")
            
