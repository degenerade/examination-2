
import player
import intelligence
import dicehand


class Game:

    def __init__(self):
        self.players = []


    def add_player(self, player_: player.Player):
        self.players.append(player_)


    def start(self, diehand: dicehand.DiceHand):
        roll = 0
        keep_going = True
        
        while keep_going:
            roll = diehand.get_roll()
            if roll == 1:
                print("Dice rolled 0, you get no point this turn.")
                break
            
            


#roll dice
# do 
# roll dice
# while != 1#