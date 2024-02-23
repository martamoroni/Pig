# TODO: how should game be displayed
"""pig dice game."""
import random


class Game:
    """game instance."""

    def __init__(self, player1, player2) -> None:
        """init the object."""
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.game_paused = False
        self.current_score = 0

    def start(self) -> bool:
        """the game loop."""
        self.print_game_state()
        while True:
            if self.rolled_one():
                continue
            if self.current_player.roll_dice(self):
                continue
            if self.current_player.pause_game:
                return self
            if self.is_game_over():
                return None
            self.change_player()
            
    def rolled_one(self) -> bool:
        """rolls the dice and check if it is a one."""
        if not self.game_paused:
            dice_roll = random.randint(1, 6)
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
        """checks if current player has more then 100 points."""
        if self.current_player.points >= 100:
            print(f"{self.current_player.name} won this game")
            return True
        return False

    def end_turn(self) -> None:
        """ends the turn of the current player."""
        self.current_player.points += self.current_score
        self.current_score = 0

    def change_player(self) -> None:
        """changes the current player."""
        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )

    def print_game_state(self) -> None:
        """displays the current game state."""
        print(f"{self.player1.name} has {self.player1.points} paonts")
        print(f"{self.player2.name} has {self.player2.points} points\n")
        print(f"{self.current_player.name}s turn\n")
