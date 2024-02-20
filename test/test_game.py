import unittest
from Pig import game
from Pig import player

"""unit test."""
class test_game(unittest.TestCase):
    """game test class"""

    def test_init(self):
        player1 = player.Player("test")
        player2 = player.Player("test2")
        game_obj = game.Game(player1, player2)
        