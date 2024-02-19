import unittest
from Pig import score_boared

class test_score_boared(unittest.TestCase):

    def test_init(self):
        res = score_boared.ScoreBoared()
        exp = score_boared.ScoreBoared
        self.assertIsInstance(res, exp)

    def test_up_date_score(self):
        boared = score_boared.ScoreBoared()
        boared.up_date_score
    
    def test_up_date_played(self):
        boared = score_boared.ScoreBoared()
        boared._up_date_game_played('test_name')
        self.assertEqual(1 == boared.players['test_name']["played"])
    
    def test_up_date_won(self):
        boared = score_boared.ScoreBoared()
        boared._up_date_game_won('test_name')
        self.assertEqual(1 == boared.players['test_name']["wins"])
 
    def test_up_date_name(self):
        boared = score_boared.ScoreBoared()
        boared._up_date_game_played('test_name')
        boared.up_date_name('test_name', 'new_name')
        self.assertFalse('test_name' in boared.players)
        self.assertTrue('new_name' in boared.players)
    
    def test_name_exists(self):
        boared = score_boared.ScoreBoared()
        boared._up_date_game_played("test_name")
        self.assertTrue(boared.name_exists("test_name"))
        self.assertFalse(boared.name_exists("test"))

    def test_load_scores(self):
        boared = score_boared.ScoreBoared()
        res = boared._load_scores("test_file.bin")
        self.assertIsInstance(dict, res)

    
 