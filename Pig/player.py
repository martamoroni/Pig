class Player():
    def __init__(self, name) -> None:
        self.name = name

    def roll_dice(self) -> bool:
        valid_choice = False

        while not valid_choice:
            choice = input("Do you want to roll the dice? (yes/no)").lower()

            if choice == "yes":
                return True
            elif choice == "no":
                return False
            else:
                print("Please enter valid choice: 'yes' or 'no'")

    def change_name(self):
        new_name = input("Set new name: ")
        self.name = new_name
