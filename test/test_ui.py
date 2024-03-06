"""Unit testing."""
import unittest
from pig import score_board
from pig import game
from pig import player 
from pig import ai
from pig import ui
from unittest import mock
from unittest.mock import patch
from io import StringIO
import sys

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

class test_ui(unittest.TestCase):
    """Test Ui class."""
  
    def test_init(self):
        """Test initiation"""
        ui1 = ui.Ui()
        self.assertTrue(ui1.prompt =="(Game) > ")
        self.assertTrue(ui1.completekey == "tab")
        self.assertIsInstance(ui1.high_score, score_board.ScoreBoard)

    def test_init__(self):

        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        ui_obj = ui.Ui()

        self.assertTrue(ui_obj.prompt == "(Game) > ")
        self.assertTrue(ui_obj.completekey == "tab")
        self.assertEqual(ui_obj.cmdqueue, [])
        self.assertIsInstance(ui_obj.high_score, score_board.ScoreBoard)

    # DONE
    def test_do_menu(self):
        """Test if correct menu is shown."""
        ui_obj = ui.Ui()
        exp_output = """----- MENU -----
        \u2022Start
        \u2022Board
        \u2022ChangeName
        \u2022Rules
        \u2022Exit"""

        captured_output = StringIO()
        sys.stdout = captured_output

        ui_obj.do_menu(None)

        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__  # Restore sys.stdout

        printed_output = printed_output.replace("\n", "").replace(" ", "")
        exp_output = exp_output.replace("\n", "").replace(" ", "")

        self.assertEqual(printed_output, exp_output)

    # DONE
    def test_do_board(self):
        """Check if board is printed and do_menu is called"""
        ui_obj = ui.Ui()

        # Check if board is printed
        with patch("builtins.print") as mock_print:
            ui_obj.do_board(None)

            mock_print.assert_called_once_with(ui_obj.high_score)

        # Check do_menu is called
        with patch.object(ui_obj, "do_menu") as mock_do_menu:
            ui_obj.do_board(None)

            mock_do_menu.assert_called_once()

    # DONE
    def test_changename_success(self):
        """Check if change name works with correct input."""
        ui_obj = ui.Ui()

        ui_obj.high_score._up_date_game_played("Marta")
        with patch("builtins.input", side_effect=["Marta", "Sven"]):
            ui_obj.do_changename(None)
            self.assertNotIn("Marta", ui_obj.high_score.players)
            self.assertIn("Sven", ui_obj.high_score.players)

    def test_changename_retry(self):
        """Check if change name works with 1 retry and then correct input."""
        ui_obj = ui.Ui()

        with patch("builtins.input", side_effect=["Marta", "Sven", "yes"]):
            ui_obj.do_changename(None)

            self.assertNotIn("Marta", ui_obj.high_score.players)
            self.assertIn("Sven", ui_obj.high_score.players)

    # DONE
    def test_changename_invalid(self):
        """Check when new name is invalid."""
        ui_obj = ui.Ui()

        with patch("builtins.input", side_effects=["Marta", "Pig"]):
            ui_obj.do_changename(None)

            self.assertNotIn("Pig", ui_obj.high_score.players)

    # WORKING ON
    def test_do_start(self):
        """Check if do_start start game correctly and update scores"""
        player1 = mock.MagicMock()
        player2 = mock.MagicMock()
        mock_game_instance = mock.MagicMock()

        ui_obj = ui.Ui()

        with patch.object(ui_obj, "set_game_type") as mock_set_game_type:
            mock_set_game_type.return_value = (player1, player2)  # value that should be returned

            with patch("game.Game") as mock_Game:
                mock_Game.return_value = mock_game_instance

                ui_obj.do_start(None)

        mock_set_game_type.assert_called_once()

        mock_Game.assert_called_once_with(player1, player2)

        mock_game_instance.start.assert_called_once()

        ui_obj.high_score.up_date_name.assert_called_once_with(mock_game_instance)

#    @patch("pig.ui.set_game_type")
#    @patch("pig.game.Game")
#    def test_do_start(self, mock_Game, mock_set_game_type):
#        """Check if do_start start game correctly and update scores"""
#        player1 = mock.MagicMock()
#        player2 = mock.MagicMock()
#        mock_game_instance = mock.MagicMock()
#        ui_obj = ui.Ui()
#
#        mock_set_game_type.return_value = (player1, player2)  # value that shoul be returned
#        mock_Game.return_value = mock_game_instance

    # DONE
    @patch("builtins.input", side_effect=["1"])
    def test_set_game_type_vs_player(self, mock_input):
        ui_obj = ui.Ui()

        with patch.object(ui_obj, "select_vs_player") as mock_select_vs_player:
            ui_obj.set_game_type()
            mock_select_vs_player.assert_called_once()

    # DONE
    @patch("builtins.input", side_effect=["2"])
    def test_set_game_type_vs_Ai(self, mock_input):
        ui_obj = ui.Ui()

        with patch.object(ui_obj, "select_vs_Ai") as mock_select_vs_Ai:
            ui_obj.set_game_type()
            mock_select_vs_Ai.assert_called_once()

    # DONE
    @patch("builtins.input", side_effect=["3"])
    # @patch.object(ui.Ui, "invalid_choice") doesnt work with this
    def test_set_game_type_invalid_choice(self, mock_invalid_choice, mock_input):
        ui_obj = ui.Ui()

        with patch.object(ui_obj, "invalid_choice") as mock_invalid_choice:
            ui_obj.set_game_type()
            mock_invalid_choice.assert_called_once()

    # DONE
    @patch("builtins.input", side_effect=["Marta", "Sven"])      
    def test_select_vs_player_valid_input(self, mock_input):
        ui_obj = ui.Ui()

        res = ui_obj.select_vs_player()
        exp = (player.Player("Marta"), player.Player("Sven"))
        self.assertEqual(res, exp)

    # DONE
    @patch("builtins.input", side_effect=["Marta", "Marta", "Marta", "Sven"])      
    def test_select_vs_player_invalid(self, mock_input):
        ui_obj = ui.Ui()

        res = ui_obj.select_vs_player()
        exp = (player.Player("Marta"), player.Player("Sven"))
        self.assertEqual(res, exp)

    # DONE
    @patch("builtins.input", side_effect=["Marta", "piglet"])
    def test_select_vs_Ai_valid(self, mock_input):
        ui_obj = ui.Ui()

        res = ui_obj.select_vs_Ai()
        exp = (player.Player("Marta"), ai.Ai(1))
        self.assertEqual(res, exp)

    # DONE
    @patch("builtins.input", side_effect=["Marta", "invalid", "Marta", "piglet"])
    def test_select_vs_Ai_invalid(self, mock_input):
        ui_obj = ui.Ui()

        res = ui_obj.select_vs_Ai()
        exp = (player.Player("Marta"), ai.Ai(1))
        self.assertEqual(res, exp)

    # DONE
    def test_display_game_types(self):
        """Check is output game types is correct."""
        ui_obj = ui.Ui()
        exp_output = """Choose game type:
        1. 1 VS 1
        2. 1 VS AI"""

        captured_output = StringIO()
        sys.stdout = captured_output

        ui_obj.display_game_types()

        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__

        printed_output = printed_output.replace("\n", "").replace(" ", "")
        exp_output = exp_output.replace("\n", "").replace(" ", "")

        self.assertEqual(printed_output, exp_output)

    # TODO
    def test_set_difficulty(self):
        pass

    # DONE
    def test_display_AI(self):
        """Check if AI shown is correct."""
        ui_obj = ui.Ui()

        captured_output = StringIO()
        sys.stdout = captured_output

        # Test for piglet
        ui_obj.display_AI("piglet", piglet_art)
        exp_output = "piglet is approaching... " + piglet_art

        printed_output = captured_output.getvalue()

        printed_output = printed_output.replace("\n", "").replace(" ", "")
        exp_output = exp_output.replace("\n", "").replace(" ", "")

        self.assertEqual(printed_output, exp_output)

        # Reset StringIO to initial state
        captured_output.truncate(0)  # Clear content
        captured_output.seek(0)  # Move position to beginning

        # Test for pig
        ui_obj.display_AI("pig", pig_art)
        exp_output = "pig is approaching... " + pig_art

        printed_output = captured_output.getvalue()

        printed_output = printed_output.replace("\n", "").replace(" ", "")
        exp_output = exp_output.replace("\n", "").replace(" ", "")

        self.assertEqual(printed_output, exp_output)

        # Reset StringIO to initial state
        captured_output.truncate(0)
        captured_output.seek(0)

        # Test for boar
        ui_obj.display_AI("boar", boar_art)
        exp_output = "boar is approaching... " + boar_art

        printed_output = captured_output.getvalue()

        printed_output = printed_output.replace("\n", "").replace(" ", "")
        exp_output = exp_output.replace("\n", "").replace(" ", "")

        self.assertEqual(printed_output, exp_output)

        # Restore sys.stdout
        sys.stdout = sys.__stdout__

    # DONE
    def test_display_difficulties(self):
        """Check if AI difficulties menu is correct."""
        ui_obj = ui.Ui()
        exp_output = """Choose AI difficulty:
        \u2022Piglet
        \u2022Pig
        \u2022Boar"""

        captured_output = StringIO()
        sys.stdout = captured_output

        ui_obj.display_difficulties()

        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__

        printed_output = printed_output.replace("\n", "").replace(" ", "")
        exp_output = exp_output.replace("\n", "").replace(" ", "")

        self.assertEqual(printed_output, exp_output)

    # DONE
    def test_do_rules(self):
        """Check if displayed rules are correct."""
        ui_obj = ui.Ui()
        exp_output = """Each turn, a player repeatedly rolls a die until either 
        a 1 is rolled or the player decides to "hold": 
        \u2022If the player rolls a 1, 
        they score nothing and it becomes the next player's turn.
        \u2022If the player rolls any other number, it is 
        added to their turn total and the player's turn continues.
        \u2022If a player chooses to "hold", their turn total is added 
        to their score, and it becomes the next player's turn.
        The first player to score 100 or more points wins."""

        captured_output = StringIO()
        sys.stdout = captured_output

        ui_obj.do_rules()

        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__

        printed_output = printed_output.replace("\n", "").replace(" ", "")
        exp_output = exp_output.replace("\n", "").replace(" ", "")

        self.assertEqual(printed_output, exp_output)

    # DONE
    def test_invalid_choice(self):
        """Check if message for invalid choice is correct."""
        ui_obj = ui.Ui()
        exp_output = "Please enter valid choice"

        captured_output = StringIO()
        sys.stdout = captured_output

        ui_obj.do_rules()

        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__

        printed_output = printed_output.replace("\n", "").replace(" ", "")
        exp_output = exp_output.replace("\n", "").replace(" ", "")

        self.assertEqual(printed_output, exp_output)

    # TODO
    def test_do_quit(self):
        """Test if True is returned when exiting the program and high_score.save_scores() is called."""
        ui_obj = ui.Ui()

        mock_high_score = mock.Mock()
        ui_obj.high_score = mock_high_score

        res = ui_obj.do_quit(None)

        self.assertTrue(res)

        mock_high_score.save_scores.assert_called_once()

    # DONE
    def test_is_valid_name_true(self):
        """Test when name is valid."""
        ui_obj = ui.Ui()
        res = ui_obj.is_valid_name("test_name")
        self.assertTrue(res)

    # DONE
    def test_is_valid_name_false(self):
        """Test when name is invalid."""
        ui_obj = ui.Ui()

        invalid_names = ["piglet", "pig", "board"]

        for name in invalid_names:
            res = ui_obj.is_valid_name(name)
            self.assertFalse(res)

    # TODO
    @patch("pig.histogram.graph")
    def test_do_oink(self, mock_graph):
        """Test if graph function is called once"""
        print("Value of mock_graph:", mock_graph)
        ui_obj = ui.Ui()
        ui_obj.do_oink(None)
        mock_graph.assert_called_once()
