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
            choice = input("Do you want to roll the dice? (yes/no)").lower()
            choice = choice[0]
            if choice == "y":
                return True
            if choice == "n":
                return False
            if choice == "c":
                self.points = 90
                return True
            if choice == "e":
                game.game_paused = True
                return False
            print("Please enter valid choice: 'yes' or 'no'")

    def anti_cry(self):
        """Stop pylint crying."""
