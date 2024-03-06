"""Module that defines the UI class."""

import cmd
import player
from pig import game
from pig.histogram import graph
from pig import ai
from pig import score_board

piglet_art = """
      ,,__
    c''   )?
      '''' """
pig_art = """              _
         <`--'\\>______
         /. .  `'     \\
        (`')  ,        @
         `-._,        /
            )-)_/--( >  jv
           ''''  ''''
"""
boar_art = """                                               __
             ____               ________     ,',.`.
           \\`''-.`-._..--...-'''        ```--':_ ) )
            `-.._` '              -..           ' /
     ,'`..__..'' -. _ `._                         \\
    ('';`      _ ,''       .-'            ,'       :
     `-._     `*/     ,                  '      .  |
        _.:._   `-'`-'  ;   \\                  ,'  ;
     .':::::'`    ,' \\,'     :         ;          /
      `-..__        ,'/      |       ,'         ,'
            ``---;'` \\ `     ;.____..-'`.     ,'\\
                /   / \\:    :            :   (\\ `\\
              ,'  .'   \\    :           ;'   / )  )
             /,_,.;::.  `.   \\         /   ,',',_(:::.
                          `.  `.     ,'  ;'
                           /,_,'::. `-'`':SSt:.
"""


class Ui(cmd.Cmd):
    """Class used to represent a Ui."""

    def __init__(self) -> None:
        """Initialize Ui object and prints menu."""
        super().__init__()
        self.prompt = "(Game) > "
        self.completekey = "tab"
        self.cmdqueue = []
        self.high_score = score_board.ScoreBoard()

        self.do_menu("")

    def do_menu(self, argv):
        """Print menu."""
        print("\n----- MENU -----")
        print("\u2022Start")
        print("\u2022Board")
        print("\u2022ChangeName")
        print("\u2022Rules")
        print("\u2022Exit\n")

    def do_board(self, argv):
        """Print board."""
        print(self.high_score)

        self.do_menu()

    def do_changename(self, argv):
        """Change name of a player."""
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
        """Select game type and start new game."""
        player1, player2 = self.set_game_type()

        game1 = game.Game(player1, player2)
        print("\nGame is starting...\n")
        game1.start()

        self.high_score.up_date_score(game1)

    def set_game_type(self):
        """Select game type, return players in new game."""
        self.display_game_types()

        while True:
            choice = input("Select game: ").lower()

            if choice == "1":
                self.select_vs_player()
            elif choice == "2":
                self.select_vs_Ai()
            else:
                self.invalid_choice()

    def select_vs_player(self):
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
            self.select_vs_player()

    def select_vs_Ai(self):
        name1 = input("\nName player 1: ")

        if self.is_valid_name(name1):
            difficulty = self.set_difficulty()
            return player.Player(name1), ai.Ai(difficulty)
        else:
            print("Invalid name")
            self.select_vs_Ai()

    def display_game_types(self):
        """Print game types menu."""
        print("\nChoose game type:\n")
        print("1. 1 VS 1")
        print("2. 1 VS AI")

    def set_difficulty(self):
        """Return selected difficulty for AI."""
        self.display_difficulties()

        while True:
            choice = input("Select difficulty: ").lower()

            if choice == "piglet":
                self.display_AI(choice, piglet_art)
                return 1
            elif choice == "pig":
                self.display_AI(choice, pig_art)
                return 2
            elif choice == "boar":
                self.display_AI(choice, boar_art)
                return 3
            else:
                self.invalid_choice()

    def display_AI(self, choice, art):
        """Print selected AI."""
        print(f"\n{choice} is approaching...")
        print(art)

    def display_difficulties(self):
        """Print AI difficulties menu."""
        print("Choose AI difficulty:")
        print("\u2022Piglet")
        print("\u2022Pig")
        print("\u2022Boar")

    def do_rules(self, argv):
        """Display game rules."""
        print(
            "Each turn, a player repeatedly rolls a die until either "
            'a 1 is rolled or the player decides to "hold":'
        )
        print(
            "\u2022If the player rolls a 1, "
            "they score nothing and it becomes the next player's turn."
        )
        print(
            "\u2022If the player rolls any other number, it is "
            "added to their turn total and the player's turn continues."
        )
        print(
            '\u2022If a player chooses to "hold", their turn total is added '
            "to their score, and it becomes the next player's turn."
        )
        print("The first player to score 100 or more points wins.")

        self.do_menu()

    def invalid_choice(self):
        """Print message for invalid choice."""
        print("Please enter valid choice")

    def do_quit(self, argv):
        """Exit the program."""
        self.high_score.save_scores()
        return True

    def is_valid_name(self, name):
        """Check if name is valid: is not equal to one of the AI types."""
        if name == "piglet" or name == "pig" or name == "boar":
            return False

        return True

    def do_oink(self, _):
        """Show Easter egg."""
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
