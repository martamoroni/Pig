import unittest
from Pig import score_boared
"""unit test."""
class test_score_boared(unittest.TestCase):
    """test score boared class."""
    def test_init(self):
        """initiates object."""
        res = score_boared.ScoreBoared()
        exp = score_boared.ScoreBoared
        self.assertIsInstance(res, exp)

    def test_up_date_score(self):
        """tests"""
        boared = score_boared.ScoreBoared()
        boared.up_date_score
    
    def test_up_date_played(self):
        """played increments by one."""
        boared = score_boared.ScoreBoared()
        boared._up_date_game_played('test_name')
        self.assertEqual(1 == boared.players['test_name']["played"])
    
    def test_up_date_won(self):
        """won increments by one."""
        boared = score_boared.ScoreBoared()
        boared._up_date_game_won('test_name')
        self.assertEqual(1 == boared.players['test_name']["wins"])
 
    def test_up_date_name(self):
        """name is updated correctly."""
        boared = score_boared.ScoreBoared()
        boared._up_date_game_played('test_name')
        boared.up_date_name('test_name', 'new_name')
        self.assertFalse('test_name' in boared.players)
        self.assertTrue('new_name' in boared.players)
    
    def test_name_exists(self):
        """name is on the boared."""
        boared = score_boared.ScoreBoared()
        boared._up_date_game_played("test_name")
        self.assertTrue(boared.name_exists("test_name"))
        self.assertFalse(boared.name_exists("test"))

    def test_load_scores_defalt(self):
        """empty dict is loaded if file is not present."""
        boared = score_boared.ScoreBoared()
        res = boared._load_scores("test_file.bin")
        self.assertIsInstance(dict, res)

    
 