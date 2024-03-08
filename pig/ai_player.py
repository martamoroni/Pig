"""Ai behaviour."""

import pickle
import random
from pig import player


class Ai(player.Player):
    """Ai instance."""

    def __init__(self, difficulty) -> None:
        """Initialize object."""
        super().__init__(None)
        self.file_name = "docs/pig_perfect_play.bin"
        self.perfect_play = None
        self.roll_dice = self.select_dificulty(difficulty)
        self.points = 0
        self.ran = random

    def load_perfect_play(self) -> None:
        """Load the perfect play instructions."""
        with open(self.file_name, "rb") as f:
            self.perfect_play = pickle.load(f)

    def select_dificulty(self, difficulty):
        """Set name for difficulty and return coresponding method."""

        def simple(_) -> bool:
            return self.ran.randint(1, 10) != 6

        def normal(game) -> bool:
            return game.current_score < 20

        def hard(game) -> bool:
            position_3d = self.perfect_play[self.points][game.player1.points]
            return position_3d > game.current_score

        match difficulty:
            case 1:
                self.name = "piglet"
                return simple
            case 2:
                self.name = "pig"
                return normal
            case 3:
                self.load_perfect_play()
                self.name = "boar"
                return hard
            case _:
                print("Error: not valid difficulty, difficulty set to normal")
                self.name = "pig"
                return normal
