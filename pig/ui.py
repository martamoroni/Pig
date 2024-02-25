import cmd, player, ai, game, score_board
from histogram import graph

piglet_art = """
      ,,__
    c''   )?
      '''' 
"""
pig_art = """              _
         <`--'\>______
         /. .  `'     \\
        (`')  ,        @
         `-._,        /
            )-)_/--( >  jv
           ''''  ''''
"""
boar_art = """                                               __
             ____               ________     ,',.`.
           \`''-.`-._..--...-'''        ```--':_ ) )
            `-.._` '              -..           ' /
     ,'`..__..'' -. _ `._                         \\
    ('';`      _ ,''       .-'            ,'       :
     `-._     `*/     ,                  '      .  |
        _.:._   `-'`-'  ;   \                  ,'  ;
     .':::::'`    ,' \,'     :         ;          /
      `-..__        ,'/      |       ,'         ,'
            ``---;'` \ `     ;.____..-'`.     ,'\\
                /   / \:    :            :   (\ `\\
              ,'  .'   \    :           ;'   / )  )
             /,_,.;::.  `.   \         /   ,',',_(:::.
                          `.  `.     ,'  ;'
                           /,_,'::. `-'`':SSt:.
"""


class Ui(cmd.Cmd):
    def __init__(self) -> None:
        """Initialize Ui object and prints menu."""
        super().__init__()
        self.prompt = "(Game) > "
        self.completekey = "tab"
        self.cmdqueue = []
        self.high_score = score_board.ScoreBoard()

        self.do_menu()

    def do_menu(self):
        """Prints menu."""
        print("\n----- MENU -----")
        print("\u2022Start")
        # print("2. Continue game")     # Might implement later
        print("\u2022Board")
        print("\u2022ChangeName")
        print("\u2022Rules")  # Have to change a bit
        print("\u2022Exit\n")

    def do_board(self, argv):
        print(self.high_score)

        self.do_menu()

    def do_changename(self, argv):
        """Changes name of a player"""
        old_name = input("Enter current name: ")
        done = False

        while not done:
            new_name = input("Enter new name: ")

            if self.is_valid_name(new_name):
                if not self.high_score.name_exists(new_name):
                    done = True
                    self.high_score.up_date_name(old_name, new_name)
                else:
                    print("Name is already used")
                    retry = input("Do you want to try again? (yes/no)").lower()

                    if retry != "yes":
                        done = True
            else:
                print("Invalid name")

        self.do_menu()

    def do_start(self, argv):
        """Selects game type and starts new game."""
        player1, player2 = self.set_game_type()

        game1 = game.Game(player1, player2)
        print("\nGame is starting...\n")
        game1.start()

        self.high_score.up_date_score(game1)


    def set_game_type(self):
        """Selects game type, returns players in new game."""
        self.display_game_types()

        valid_choice = False

        while not valid_choice:
            choice = input("Select game: ").lower()

            match choice:
                case "1":
                    name1 = input("\nName player 1: ")
                    name2 = input("Name player 2: ")

                    if (
                        self.is_valid_name(name1)
                        and self.is_valid_name(name2)
                        and name1 != name2
                    ):
                        return player.Player(name1), player.Player(name2)
                    else:
                        print("Invalid name")
                case "2":
                    name1 = input("\nName player 1: ")

                    if self.is_valid_name(name1):
                        difficulty = self.set_difficulty()
                        return player.Player(name1), ai.Ai(difficulty)
                    else:
                        print("Invalid name")
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
            choice = input("Select difficulty: ").lower()

            match choice:
                case "piglet":
                    self.display_AI(choice, piglet_art)
                    return 1
                case "pig":
                    self.display_AI(choice, pig_art)
                    return 2
                case "boar":
                    self.display_AI(choice, boar_art)
                    return 3
                case _:
                    print("\033[A                             \033[A")
                    self.invalid_choice()

    def display_AI(self, choice, art):
        print(f"\n{choice} is approaching...")
        print(art)

    def display_difficulties(self):
        """Prints AI difficulties menu."""
        print("Choose AI difficulty:")
        print("\u2022Piglet")
        print("\u2022Pig")
        print("\u2022Boar")

    def do_rules(self, argv):
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

        self.do_menu()

    def invalid_choice(self):
        """Prints message for invalid choice"""
        print("Please enter valid choice")

    def do_quit(self, argv):
        """Exits the program"""
        self.high_score.save_scores()
        return True

    def is_valid_name(self, name):
        if name == "piglet" or name == "pig" or name == "boar":
            return False

        return True

    def do_oink(self, _):
        graph()

    # aliasing
    do_Menu = do_menu
    do_Quit = do_quit
    do_Exit = do_quit
    do_exit = do_quit
    do_Start = do_start
    do_Board = do_board
    do_ChangeName = do_changename
    do_Rules = do_rules
