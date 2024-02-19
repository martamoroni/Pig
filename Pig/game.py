# TODO: how should game be displayed
import random

class Game():
    def __init__(self, player1, player2) -> None:
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.game_paused = False
        self.current_score = 0
        self.ran = random()

    def start(self) -> bool:
        self.print_game_state()
        while True:
            if self.rolled_one():
                continue
            if self.current_turn.roll_dice(self):
                continue
            if self.current_turn.pause_game:
                return self
            if self.is_game_over():
                return None
            self.change_player()

    def rolled_one(self) -> bool:
        if not self.game_paused:
            dice_roll = self.ran.ranint(1, 6)
            print(f"the dice roll is {dice_roll}")
            if dice_roll == 1:
                self.current_score = 0
                self.change_player()
                return True
            self.current_score += dice_roll
        else:
            self.game_paused = False
        return False

    def is_game_over(self) -> bool:
        if self.current_turn.points >= 100:
            print(f"{self.current_player.name} won this game")
            return True
        return False

    def end_turn(self) -> None:
        self.current_turn.points += self.current_score
        self.current_score = 0

    def change_player(self) -> None:
        self.current_turn = self.player2 if self.current_player == self.player1 else self.player1
    
    def print_game_state(self) -> None:
        print(f"{self.player1.name} has {self.player1.points} paonts")
        print(f"{self.player2.name} has {self.player2.points} points\n")
        print(f"{self.current_turn.name}s turn\n")
        