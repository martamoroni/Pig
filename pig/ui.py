"""Module that defines the UI class."""

import cmd
from pig import player
from pig import game
from pig.histogram import graph
from pig import ai
from pig import score_board

PIGLET_ART = """
      ,,__
    c''   )?
      '''' """
PIG_ART = """              _
         <`--'\\>______
         /. .  `'     \\
        (`')  ,        @
         `-._,        /
            )-)_/--( >  jv
           ''''  ''''
                    """
BOAR_ART = """                                               __
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

        self.do_menu(None)

    def do_menu(self, _):
        """Print menu."""
        print(
            "\n----- MENU -----\n"
            "- Start\n"
            "- Board\n"
            "- ChangeName\n"
            "- Rules\n"
            "- Exit\n"
        )

    def do_board(self, _):
        """Print board."""
        print(self.high_score)

        self.do_menu(None)

    def do_changename(self, _):
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

        self.do_menu(None)

    def do_start(self, _):
        """Select game type and start new game."""
        player1, player2 = self.set_game_type()

        game1 = game.Game(player1, player2)
        print("\nGame is starting...\n")
        game1.start()

        if game1.is_game_over():
            print(f"{game1.current_player.name} won this game")
            self.high_score.up_date_score(game1)

    def set_game_type(self):
        """Select game type, return players in new game."""
        self.display_game_types()

        while True:
            choice = input("Select game: ").lower()

            if choice == "1":
                return self.select_vs_player()
            if choice == "2":
                return self.select_vs_ai()
            self.invalid_choice()

    def select_vs_player(self):
        """Select player names."""
        name1 = input("\nName player 1: ")
        name2 = input("Name player 2: ")

        valid_names = self.is_valid_name(name1) and self.is_valid_name(name2)
        if valid_names and name1 != name2:
            return player.Player(name1), player.Player(name2)
        print("Invalid name")
        return self.select_vs_player()

    def select_vs_ai(self):
        """Select player name and Ai."""
        name1 = input("\nName player 1: ")

        if self.is_valid_name(name1):
            difficulty = self.set_difficulty()
            return player.Player(name1), ai.Ai(difficulty)
        print("Invalid name")
        return self.select_vs_ai()

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
                self.display_ai(choice, PIGLET_ART)
                return 1
            if choice == "pig":
                self.display_ai(choice, PIG_ART)
                return 2
            if choice == "boar":
                self.display_ai(choice, BOAR_ART)
                return 3
            self.invalid_choice()

    def display_ai(self, choice, art):
        """Print selected AI."""
        print(f"\n{choice} is approaching...")
        print(art)

    def display_difficulties(self):
        """Print AI difficulties menu."""
        print("Choose AI difficulty:")
        print("- Piglet")
        print("- Pig")
        print("- Boar")

    def do_rules(self, _):
        """Display game rules."""
        print("Each turn, a player can choose to either roll a die or hold:")
        print(
            "If a player decides to hold, the turn score is added to their "
            "total score and it becomes the next player's turn."
        )
        print(
            "If the player rolls 1, they score nothing "
            "and it becomes the next player's turn."
        )
        print(
            "If a player rolls any other number, that number is added to "
            "their turn score and their turn continues."
        )
        print("To win the game a player has to score 100 or more points.")

        self.do_menu(None)

    def invalid_choice(self):
        """Print message for invalid choice."""
        print("Please enter valid choice")

    def do_quit(self, _):
        """Exit the program."""
        self.high_score.save_scores()
        return True

    def is_valid_name(self, name):
        """Check if name is valid: is not equal to one of the AI types."""
        if name in ("piglet", "pig", "boar"):
            return False

        return True

    def do_oink(self, _):
        """Show Easter egg."""
        graph()

    def default(self, line):
        """Overwrite defailt."""
        print("invalid choice")

    # aliasing
    do_Menu = do_menu
    do_Quit = do_quit
    do_Exit = do_quit
    do_exit = do_quit
    do_Start = do_start
    do_Board = do_board
    do_ChangeName = do_changename
    do_Rules = do_rules
