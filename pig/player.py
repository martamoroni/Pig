"""Player super class."""


class Player:
    """Player super class instance."""

    def __init__(self, name) -> None:
        """Class init."""
        self.name: str = name
        self.score = 0

    def roll_dice(self, game):
        """Dont look."""

    def anti_cry(self):
        """Stop pylint crying."""
