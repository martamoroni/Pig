import unittest
from pig import player
from unittest import mock
from pig import game
from io import StringIO
import sys


class test_player(unittest.TestCase):

    def test_init(self) -> None:
        player1 = player.Player("Marta")
        exp = player.Player
        self.assertIsInstance(player1, exp)

        res = player1.name
        exp = "Marta"
        self.assertEqual(res, exp)

        res = player1.points
        exp = 0
        self.assertEqual(res, exp)

    def test_roll_dice_yes(self):
        player1 = player.Player("test_name")
        player2 = player.Player("test_name2")
        game_obj = game.Game(player1, player2)
        with mock.patch("builtins.input", return_value="yes"):
            self.assertTrue(player1.roll_dice(game_obj))

    def test_roll_dice_no(self):
        player1 = player.Player("test_name")
        player2 = player.Player("test_name2")
        game_obj = game.Game(player1, player2)
        with mock.patch("builtins.input", return_value="no"):
            self.assertFalse(player1.roll_dice(game_obj))

    def test_roll_dice_exit(self):
        player1 = player.Player("test_name")
        player2 = player.Player("test_name2")
        game_obj = game.Game(player1, player2)
        with mock.patch("builtins.input", return_value="exit"):
            self.assertFalse(player1.roll_dice(game_obj))
            self.assertTrue(game_obj.game_paused)

    def test_roll_dice_cheat(self):
        player1 = player.Player("test_name")
        player2 = player.Player("test_name2")
        game_obj = game.Game(player1, player2)
        with mock.patch("builtins.input", return_value="cheat"):
            self.assertTrue(player1.roll_dice(game_obj))
            self.assertTrue(player1.points == 90)

    def test_roll_dice_invalid(self):
        player1 = player.Player("test_name")
        player2 = player.Player("test_name2")
        game_obj = game.Game(player1, player2)

        with mock.patch("builtins.input", side_effect=["test", "y"]):
            captured_output = StringIO()
            sys.stdout = captured_output

            exp = player1.roll_dice(game_obj)

            sys.stdout = sys.__stdout__
            out = captured_output.getvalue()
            self.assertTrue(exp)
            self.assertTrue("Please enter valid choice" in out)
