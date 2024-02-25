"""unit test."""

import unittest
from pig import score_board
from pig import game
from pig import ai
import os


class test_score_boared(unittest.TestCase):
    """test score boared class."""

    def test_init(self):
        """initiates object."""
        res = score_board.ScoreBoard()
        exp = score_board.ScoreBoard
        self.assertIsInstance(res, exp)

    def test_up_date_score(self):
        """tests"""
        boared = score_board.ScoreBoard()
        p1 = ai.Ai(1)
        p2 = ai.Ai(2)
        game_obj = game.Game(p1, p2)
        boared.up_date_score(game_obj)
        self.assertTrue(1 == boared.players[game_obj.player1.name]["played"])
        self.assertTrue(1 == boared.players[game_obj.player2.name]["played"])
        self.assertTrue(1 == boared.players[game_obj.player1.name]["wins"])

    def test_up_date_played(self):
        """played increments by one."""
        boared = score_board.ScoreBoard()
        boared._up_date_game_played("test_name")
        self.assertEqual(1, boared.players["test_name"]["played"])

    def test_up_date_won(self):
        """won increments by one."""
        boared = score_board.ScoreBoard()
        boared._up_date_game_won("test_name")
        self.assertEqual(1, boared.players["test_name"]["wins"])

    def test_up_date_name(self):
        """name is updated correctly."""
        boared = score_board.ScoreBoard()
        boared._up_date_game_played("test_name")
        boared.up_date_name("test_name", "new_name")
        self.assertFalse("test_name" in boared.players)
        self.assertTrue("new_name" in boared.players)

    def test_name_exists(self):
        """name is on the boared."""
        boared = score_board.ScoreBoard()
        boared._up_date_game_played("test_name")
        self.assertTrue(boared.name_exists("test_name"))
        self.assertFalse(boared.name_exists("test"))

    def test_load_scores_defalt(self):
        """empty dict is loaded if file is not present."""
        boared = score_board.ScoreBoard()
        res = boared._load_scores("test_file.bin")
        self.assertIsInstance(res, dict)

    def test_save_scores(self):
        boared = score_board.ScoreBoard()
        boared.file_name = "docs/test_file.bin"
        boared.save_scores(boared.file_name)
        self.assertTrue(os.path.exists("docs/test_file.bin"))
        os.remove("docs/test_file.bin")

    def test_string(self):
        boared = score_board.ScoreBoard()
        boared._up_date_game_played("test")
        boared._up_date_game_played("test")
        boared._up_date_game_won("test")
        print(boared)
        self.assertTrue("50" in boared.__str__())
