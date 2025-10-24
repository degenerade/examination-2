from typing import Optional

from .highscore import HighScore
from .player import Player


class Game:
    WINNING_SCORE = 100

    def __init__(self, players, dice_hand, highscore: Optional[HighScore] = None):
        if not players:
            raise ValueError("Game requires at least one player.")
        if dice_hand is None:
            raise ValueError("Game requires a dice hand.")
        self.players = players
        self.dice_hand = dice_hand
        self.highscore = highscore
        self.current_player_index = 0
        self.game_over = False

    def current_player(self) -> Player:
        """returns the current player object"""
        return self.players[self.current_player_index]

    def switch_turn(self):
        """Swtich to the other players turn"""
        if not self.players:
            return
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def take_turn(self):
        """Single turn for the current player"""
        player = self.current_player()
        print(f"\n\n--->{player.name}'s turn!")
        if player.intelligence is None:
            raise ValueError(f"Player {player.name} does not have a strategy assigned.")

        while True:
            choice = player.intelligence.decide_action(player, self, self.dice_hand).strip().lower()
            
            if choice == "q":
                print("\nYou ended the game early. Returning to menu...")
                self.game_over = True
                return

            if choice == "+":
                player.total_score += 10
                print(f"Added 10 points... Cheater... Total score: {player.total_score}")
                continue

            if choice == "r":
                roll = self.dice_hand.get_roll()
                print(
                    f"{player.name} rolled {self.dice_hand.previous_roll} (total {roll})"
                )

                if 1 in self.dice_hand.previous_roll:
                    print("Uh oh, u rolled a 1 ⚀... No turn for you.")
                    player.lose_turn()
                    break
                else:
                    player.add_turn_points(roll)
                    print(f"Turn total: {player.turn_score}")

            elif choice == "h":
                player.bank_turn()
                print(f"{player.name} banks points. Total score: {player.total_score}")
                break

        if player.total_score >= self.WINNING_SCORE:
            self._handle_win(player)
        else:
            self.switch_turn()

    def play(self):
        """main loop to play game"""
        while not self.game_over:
            self.take_turn()
        
        if not self.game_over or all(p.total_score < self.WINNING_SCORE for p in self.players):
            print("\nGame ended without a winner :(.)")
        self._display_histogram()
        self._display_highscores()

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

    def _handle_win(self, player: Player) -> None:
        print(f"{player.name} wins!!! They won with {player.total_score} points!")
        self.game_over = True
        if self.highscore:
            try:
                for contender in self.players:
                    won = contender is player
                    self.highscore.record_game(contender.name, contender.total_score, won=won)
            except Exception as exc:
                print(f"Could not save high score: {exc}")

    def _display_highscores(self, limit: int = 10) -> None:
        if not self.highscore:
            return
        try:
            entries = self.highscore.top(limit)
        except Exception as exc:
            print(f"\nCould not read high scores: {exc}")
            return
        if not entries:
            return

        print("\nHigh Scores:")
        for idx, entry in enumerate(entries, start=1):
            games = entry["games_played"]
            avg = entry["total_score"] / games if games else 0
            print(
                f"{idx:>2}. {entry['display_name']:15} "
                f"best: {entry['best_score']:3d} | "
                f"wins: {entry['wins']:2d}/{games:2d} | "
                f"avg: {avg:5.1f}"
            )
