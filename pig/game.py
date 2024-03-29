"""Pig dice game."""

import random
from pig.player import Player


class Game:
    """Game instance."""

    def __init__(self, player1: Player, player2: Player) -> None:
        """Initialize the object."""
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.game_paused = False
        self.current_score = 0
        self.ran = random

    def start(self) -> bool:
        """Game loop."""
        print("| Roll dice | | Cheat | Exit |")
        self.print_game_state()
        while True:
            dice_roll = self.ran.randint(1, 6)
            if self.rolled_one(dice_roll):
                continue
            if self.current_player.roll_dice(self):
                continue
            if self.game_paused:
                return False
            self.end_turn()
            if self.is_game_over():
                return True
            self.change_player()

    def rolled_one(self, dice_roll) -> bool:
        """Roll the dice and check if it is a one."""
        if not self.game_paused:
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
        """Check if current player has more then 100 points."""
        if self.current_player.points >= 100:
            return True
        return False

    def end_turn(self) -> None:
        """End the turn of the current player."""
        self.current_player.points += self.current_score
        self.current_score = 0

    def change_player(self) -> None:
        """Change the current player."""
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
        self.print_game_state()

    def print_game_state(self) -> None:
        """Display the current game state."""
        print(f"\n{self.player1.name} has {self.player1.points} points")
        print(f"{self.player2.name} has {self.player2.points} points\n")
        print(f"{self.current_player.name}'s turn\n")
