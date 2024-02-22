import cmd, player, ai, game

class Ui(cmd.Cmd):
    def __init__(self) -> None:
        super().__init__()
        self.prompt = "(Game) > "
        self.completekey = "tab"
        self.cmdqueue = []

        self.in_menu = False

        self.initialization_menu()


    def initialization_menu(self):
        print("\nWelcome to PIG!")
        self.do_MENU(self)


    def do_MENU(self, argv):
        self.display_menu()
        self.get_menu_choice()
        
        self.in_menu = True

    
    def display_menu(self):
        print("\n----- MENU -----")
        print("1. Start")               # Done
        # print("2. Continue game")     # Might implement later
        print("3. Board")               #
        print("4. Change name")         # 
        print("5. Rules")               #
        print("6. Exit\n")              # Done


    def get_menu_choice(self):
        choice = input("Enter choice: ").lower()

        match choice:
            case "1", "start":
                self.start_game()
            case "2", "continue game":
                pass
            case "3", "board":
                pass
            case "4", "change name":
                pass
            case "5", "rules":
                self.display_rules()
            case "6", "exit":
                self.do_Quit()
            case _:
                self.invalid_choice


    def start_game(self):
        player1, player2 = self.set_game_type()

        game.Game(player1, player2)


    def set_game_type(self):
        self.display_game_types()

        valid_choice = False

        while not valid_choice:
            choice = input("Select game: ").lower()

            match choice:
                case "1 vs 1":
                    name1 = input("Name player 1: ")
                    name2 = input("Name player 2: ")
                    return player.Player(name1), player.Player(name2) 
                case "1 vs ai":
                    name1 = input("Name player 1: ")
                    difficulty = self.set_difficulty()
                    return player.Player(name1), ai.Ai(difficulty)
                case _:
                    self.invalid_choice()


    def display_game_types(self):
        print("\nChoose game type:\n")
        print("1. 1 VS 1")
        print("2. 1 VS AI")


    def set_difficulty(self):
        self.display_difficulties()

        valid_choice = False

        while not valid_choice:
            choice = input("Select game: ").lower()

            match choice:
                case "1", "piglet":
                    return "piglet"
                case "2", "pig":
                    return "pig"
                case "1", "boar":
                    return "boar"
                case _:
                    self.invalid_choice()


    def display_difficulties(self):
        print("\nChoose difficulty:\n")
        print("1. Piglet")
        print("2. Pig")
        print("3. Boar")


    def invalid_choice(self):
        print("Please enter valid choice")


    def do_Quit(self, argv):
        """This exits the program"""
        return True
    
    
    #aliasing
    do_menu = do_MENU
    do_quit = do_Quit
    do_6 = do_Quit