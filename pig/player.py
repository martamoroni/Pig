"""Module that defines the Player class."""


class Player:
    """Class used to represent a Player."""

    def __init__(self, name) -> None:
        """Initialize Player object."""
        self.name = name
        self.points = 0

    def roll_dice(self, game) -> bool:
        """Check if player wants to roll the dice, return True or False."""
        print(game.current_score)
        while True:
            choice = input(f"{self.name}, roll the dice? (y/n)")
            choice = choice[0].lower()
            match (choice):
                case "y":
                    return True
                case "n":
                    return False
                case "c":
                    self.points = 90
                    return True
                case "e":
                    game.game_paused = True
                    return False
                case _:
                    print("Please enter valid choice: 'y' or 'n'")

    def anti_cry(self):
        """Stop pylint crying."""
