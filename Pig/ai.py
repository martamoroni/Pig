"""game ai behaviour."""

import pickle
import random


class Ai:
    """ai instance."""

    def __init__(self, difficulty) -> None:
        """initiation object."""
        self.name = None
        self.file_name = "pig_perfect_play.bin"
        self.perfect_play = None
        self.roll_dice = self.select_dificulty(difficulty)
        self.points = 0

    def load_perfect_play(self) -> None:
        """load the perfect play instructions."""
        with open(self.file_name, "rb") as f:
            self.perfect_play = pickle.load(f)

    def select_dificulty(self, difficulty):
        """set name for dificulty and returns coresponding method."""

        def simple(game) -> bool:
            return random.randint(1, 10) != 6

        def normal(game) -> bool:
            return game.current_score < 20

        def hard(game) -> bool:
            return (
                self.perfect_play[self.points][game.player1.points] > game.current_score
            )

        match difficulty:
            case 1:
                self.name = "pig-let"
                return simple
            case 2:
                self.name = "pig"
                return normal
            case 3:
                self.load_perfect_play()
                self.name = "Boar"
                return hard
            case _:
                print("error: not valid difficulty, difficulty set to normal")
                self.name = "pig"
                return normal
