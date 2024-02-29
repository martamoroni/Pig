"""Module that defines the Player class."""


class Player:
    """Class used to represent a Player."""

    def __init__(self, name) -> None:
        """Initialize Player object."""
        self.name = name
        self.points = 0

    def roll_dice(self, game) -> bool:
        """Check if player wants to roll the dice, return True or False."""
        valid_choice = False
        print(game.current_score)
        while not valid_choice:
            choice = input("Do you want to roll the dice? (yes/no)").lower()
            choice = choice[0]
            if choice == "y":
                return True
            elif choice == "n":
                return False
            elif choice == "c":
                self.points = 90
                return True
            elif choice == "e":
                game.game_paused = True
                return False
            else:
                print("Please enter valid choice: 'yes' or 'no'")

