import unittest
from pig import game
from pig import player
from pig import ai
from unittest import mock


class test_game(unittest.TestCase):

    def test_init(self):
        player1 = player.Player("test")
        player2 = player.Player("test2")
        game_obj = game.Game(player1, player2)
        self.assertTrue(game_obj.player1 == player1)
        self.assertTrue(game_obj.player2 == player2)
        self.assertTrue(game_obj.current_player == player1)
        self.assertTrue(game_obj.current_score == 0)

    def test_is_game_over(self):
        player1 = player.Player("test")
        player2 = player.Player("test2")
        game_obj = game.Game(player1, player2)
        player1.points = 100
        self.assertTrue(game_obj.is_game_over())
        game_obj.current_player = player2
        self.assertFalse(game_obj.is_game_over())

    def test_end_turn(self):
        player1 = player.Player("test")
        player2 = player.Player("test2")
        game_obj = game.Game(player1, player2)
        game_obj.current_score = 10
        game_obj.end_turn()
        self.assertTrue(game_obj.current_score == 0)
        self.assertTrue(player1.points == 10)

    def test_change_player(self):
        player1 = player.Player("test")
        player2 = player.Player("test2")
        game_obj = game.Game(player1, player2)
        game_obj.change_player()
        self.assertTrue(game_obj.current_player == player2)

    def test_rolled_one_paused(self):
        player1 = player.Player("test")
        player2 = player.Player("test2")
        game_obj = game.Game(player1, player2)
        game_obj.game_paused = True

        self.assertFalse(game_obj.rolled_one(3))
        self.assertFalse(game_obj.game_paused)

    def test_rolled_one_not_paused(self):
        player1 = player.Player("test")
        player2 = player.Player("test2")
        game_obj = game.Game(player1, player2)
        self.assertTrue(game_obj.rolled_one(1))
        self.assertTrue(game_obj.current_score == 0)
        self.assertFalse(game_obj.rolled_one(6))
        self.assertTrue(game_obj.current_score == 6)

    def test_start_paused(self):
        player1 = player.Player("test")
        player2 = ai.Ai(2)
        game_obj = game.Game(player1, player2)
        game_obj.current_score = 30
        with mock.patch("builtins.input", return_value="exit"):
            self.assertFalse(game_obj.start())

    def test_start_loop(self):
        player1 = ai.Ai(2)
        player2 = ai.Ai(2)
        game_obj = game.Game(player1, player2)
        game_obj.current_score = 30
        game_obj.ran.seed(14)

    def test_start_win(self):
        player1 = ai.Ai(2)
        player2 = ai.Ai(2)
        player1.points = 76
        game_obj = game.Game(player1, player2)
        game_obj.current_score = 30
        player1.points = 100
        self.assertTrue(game_obj.start())
