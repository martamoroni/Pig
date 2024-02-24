class Player:
    def __init__(self, name) -> None:
        """Initialize Player object."""
        self.name = name
        self.points = 0

    def roll_dice(self, game) -> bool:
        """Checks if player wants to roll the dice, return True or False."""
        valid_choice = False
        print(game.current_score)
        while not valid_choice:
            choice = input("Do you want to roll the dice? (yes/no)").lower()

            if choice == "yes":
                return True
            elif choice == "no":
                return False 
            elif choice == "cheating":
                self.points = 90
            elif choice == "exit":
                game.game_paused = True
            else:
                print("Please enter valid choice: 'yes' or 'no'")

    def change_name(self):
        """Changes player name."""
        new_name = input("Set new name: ")
        self.name = new_name
