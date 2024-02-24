import cmd, player, ai, game, score_boared


class Ui(cmd.Cmd):
    def __init__(self) -> None:
        """Initialize Ui object and prints menu."""
        super().__init__()
        self.prompt = "(Game) > "
        self.completekey = "tab"
        self.cmdqueue = []
        self.high_score = score_boared.ScoreBoared()

        self.do_menu()

    def initialization_menu(self):
        """Displays starting menu."""
        print("\nWelcome to PIG!")
        self.do_MENU(self)

    def do_MENU(self, argv):
        """Prints menu and gets user choice."""
        self.display_menu()
        self.get_menu_choice()

    def do_menu(self):
        """Prints menu."""
        print("\n----- MENU -----")
        print("1. Start")  # Done
        # print("2. Continue game")     # Might implement later
        print("3. Board")  # Done
        print("4. Change name")  # Question
        print("5. Rules")  # Have to change a bit
        print("6. Exit\n")  # Done

    def do_board(self):
        print(self.high_score)


    def do_change(self):
        pass


    def do_start(self):
        """Selects game type and starts new game."""
        player1, player2 = self.set_game_type()

        game1 = game.Game(player1, player2)
        game1.start()

        self.high_score.up_date_score(game1)

    def set_game_type(self):
        """Selects game type, returns players in new game."""
        self.display_game_types()

        valid_choice = False

        while not valid_choice:
            choice = input("Select game: ").lower()

            match choice:
                case "1 vs 1":
                    name1 = input("Name player 1: ")
                    name2 = input("Name player 2: ")
                    return player.Player(name1), player.Player(name2)
                case "2":
                    name1 = input("Name player 1: ")
                    difficulty = self.set_difficulty()
                    return player.Player(name1), ai.Ai(difficulty)
                case _:
                    self.invalid_choice()

    def display_game_types(self):
        "Prints game types menu."
        print("\nChoose game type:\n")
        print("1. 1 VS 1")
        print("2. 1 VS AI")

    def set_difficulty(self):
        """Returns selected difficulty for AI."""
        self.display_difficulties()

        valid_choice = False

        while not valid_choice:
            choice = input("Select game: ").lower()

            match choice:
                case "1", "piglet":
                    return 1
                case "2", "pig":
                    return 2
                case "3":
                    return 3
                case _:

    def display_difficulties(self):
        """Prints AI difficulties menu."""
        print("\nChoose difficulty:\n")
        print("1. Piglet")
        print("2. Pig")
        print("3. Boar")

    def do_rules(self):
        """Displays game rules."""
        print(
            'Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":'
        )
        print(
            "\u2022If the player rolls a 1, they score nothing and it becomes the next player's turn."
        )
        print(
            "\u2022If the player rolls any other number, it is added to their turn total and the player's turn continues."
        )
        print(
            '\u2022If a player chooses to "hold", their turn total is added to their score, and it becomes the next player\'s turn.'
        )
        print("The first player to score 100 or more points wins.")

    def invalid_choice(self):
        """Prints message for invalid choice"""
        print("Please enter valid choice")

    def do_Quit(self, argv):
        """Exits the program"""
        return True

    # aliasing
    do_menu = do_MENU
    do_quit = do_Quit
    do_6 = do_Quit