"""Unit testing."""

import cmd
from pig import player
from pig import ai
from pig import game
from pig import score_board
from pig.histogram import graph
import unittest
from pig import ui
from unittest import mock

class test_ui(unittest.TestCase):
    """Test Ui class."""

    #TODO
    def test_init__(self) -> None:
        """Initialize Ui object and prints menu."""
        super().__init__()
        self.prompt = "(Game) > "
        self.completekey = "tab"
        self.cmdqueue = []
        self.high_score = score_board.ScoreBoard()

    #TODO
    def do_menu(self):
        """Print menu."""
        print("\n----- MENU -----")
        print("\u2022Start")
        print("\u2022Board")
        print("\u2022ChangeName")
        print("\u2022Rules")
        print("\u2022Exit\n")

    #TODO
    def do_board(self, argv):
        """Print board."""
        print(self.high_score)

        self.do_menu()
    
    def test_changename_success(self, argv):
        """Check if change name works with correct input"""
        ui1 = ui.Ui()

        with mock.patch("builtins.input", side_effect=["Marta", "Sven"]):
            self.high_score.up_date_name("Marta", "Sven")

            ui1.do_changename()

            self.assertNotIn("Marta", self.high_score.players)
            self.assertIn("Sven", self.high_score.players)

    def test_changename_retry(self, argv):
        """Check if change name works with 1 retry and then correct input"""
        ui1 = ui.Ui()

        with mock.patch("builtins.input", side_effects=["Marta", "Sven", "yes"]):
            ui1.do_changename()

            self.assertNotIn("Marta", self.high_score.players)
            self.assertIn("Sven", self.high_score.players)
        
    def test_changename_invalid(self, argv):
        """Check when new name is invalid"""
        ui1 = ui.Ui()

        with mock.patch("builtins.input", side_effects=["Marta", "Pig"]):
            ui1.do_changename()

            self.assertNotIn("Pig", self.high_score.players)

    #TODO
    def test_do_start(self, argv):
        pass   

    #TODO
    def do_start(self, argv):
        """Select game type and start new game."""
        player1, player2 = self.set_game_type()

        game1 = game.Game(player1, player2)
        print("\nGame is starting...\n")
        game1.start()

        self.high_score.up_date_score(game1)

    #TODO
    def set_game_type(self):
        """Select game type, return players in new game."""
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

    #TODO
    def display_game_types(self):
        """Check is output game types is correct"""
        exp = """\nChoose game type:\n\n
        1. 1 VS 1\n
        2. 1 VS AI"""

        

        """Print game types menu."""
        print("\nChoose game type:\n")
        print("1. 1 VS 1")
        print("2. 1 VS AI")

    #TODO
    def set_difficulty(self):
        """Return selected difficulty for AI."""
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

    #TODO
    def display_AI(self, choice, art):
        """Print selected AI."""
        print(f"\n{choice} is approaching...")
        print(art)

    #TODO
    def display_difficulties(self):
        """Print AI difficulties menu."""
        print("Choose AI difficulty:")
        print("\u2022Piglet")
        print("\u2022Pig")
        print("\u2022Boar")

    #TODO
    def do_rules(self, argv):
        """Display game rules."""
        print(
            """Each turn, a player repeatedly rolls a die until either """
            """a 1 is rolled or the player decides to "hold":"""
        )
        print(
            """\u2022If the player rolls a 1, """
            """they score nothing and it becomes the next player's turn."""
        )
        print(
            """\u2022If the player rolls any other number, it is """
            """added to their turn total and the player's turn continues."""
        )
        print(
            '\u2022If a player chooses to "hold", their turn total is added '
            ""
            """to their score, and it becomes the next player\'s turn."""
        )
        print("The first player to score 100 or more points wins.")

        self.do_menu()

    #TODO
    def invalid_choice(self):
        """Print message for invalid choice."""
        print("Please enter valid choice")

    #TODO
    def do_quit(self, argv):
        """Exit the program."""
        self.high_score.save_scores()
        return True

    #TODO
    def is_valid_name(self, name):
        """Check if name is valid: is not equal to one of the AI types."""
        if name == "piglet" or name == "pig" or name == "boar":
            return False

        return True

    #TODO
    def do_oink(self, _):
        """Show Easter egg."""
        graph()