import unittest
from pig import score_board
from pig import game
from pig import ai_player
import os


class test_score_board(unittest.TestCase):

    def test_init(self):
        res = score_board.ScoreBoard()
        exp = score_board.ScoreBoard
        self.assertIsInstance(res, exp)

    def test_up_date_score(self):
        board = score_board.ScoreBoard()
        p1 = ai_player.Ai(1)
        p2 = ai_player.Ai(2)
        board.players = board._load_scores("")
        game_obj = game.Game(p1, p2)
        board.up_date_score(game_obj)
        self.assertTrue(1 == board.players[game_obj.player1.name]["played"])
        self.assertTrue(1 == board.players[game_obj.player2.name]["played"])
        self.assertTrue(1 == board.players[game_obj.player1.name]["wins"])

    def test_up_date_played(self):
        board = score_board.ScoreBoard()
        board._up_date_game_played("test_name")
        self.assertEqual(1, board.players["test_name"]["played"])

    def test_up_date_won(self):
        board = score_board.ScoreBoard()
        board._up_date_game_won("test_name")
        self.assertEqual(1, board.players["test_name"]["wins"])

    def test_up_date_name(self):
        board = score_board.ScoreBoard()
        board._up_date_game_played("test_name")
        board.up_date_name("test_name", "new_name")
        self.assertFalse("test_name" in board.players)
        self.assertTrue("new_name" in board.players)

    def test_name_exists(self):
        board = score_board.ScoreBoard()
        board._up_date_game_played("test_name")
        self.assertTrue(board.name_exists("test_name"))
        self.assertFalse(board.name_exists("test"))

    def test_load_scores_defalt(self):
        board = score_board.ScoreBoard()
        res = board._load_scores("test_file.bin")
        self.assertIsInstance(res, dict)

    def test_save_scores(self):
        board = score_board.ScoreBoard()
        board.file_name = "docs/test_file.bin"
        board.save_scores(board.file_name)
        self.assertTrue(os.path.exists("docs/test_file.bin"))
        os.remove("docs/test_file.bin")

    def test_string(self):
        board = score_board.ScoreBoard()
        board._up_date_game_played("test")
        board._up_date_game_played("test")
        board._up_date_game_won("test")
        self.assertTrue("50" in board.__str__())
