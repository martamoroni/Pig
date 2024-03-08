import unittest
from pig import ai
from pig import game


class test_ai(unittest.TestCase):

    def test_init(self):
        res = ai.Ai(1)
        exp = ai.Ai
        self.assertIsInstance(res, exp)
        self.assertTrue(res.perfect_play is None)

    def test_select_dificulty_1(self):
        ai_obj = ai.Ai(1)
        res = ai_obj.select_dificulty(1).__name__
        exp = "simple"
        self.assertEqual(exp, res)
        self.assertEqual("piglet", ai_obj.name)

    def test_select_dificulty_2(self):
        ai_obj = ai.Ai(2)
        res = ai_obj.select_dificulty(2).__name__
        exp = "normal"
        self.assertEqual(exp, res)
        self.assertEqual("pig", ai_obj.name)

    def test_select_dificulty_3(self):
        ai_obj = ai.Ai(3)
        res = ai_obj.select_dificulty(3).__name__
        exp = "hard"
        self.assertEqual(exp, res)
        self.assertEqual("boar", ai_obj.name)

    def test_invalid_dificulty(self):
        ai_obj = ai.Ai(8)
        res = ai_obj.select_dificulty(2).__name__
        exp = "normal"
        self.assertEqual(exp, res)
        self.assertEqual("pig", ai_obj.name)

    def test_load_file(self):
        ai_obj = ai.Ai(1)
        ai_obj.load_perfect_play()
        self.assertIsInstance(ai_obj.perfect_play, dict)

    def test_normal_ai(self):
        ai_obj = ai.Ai(2)
        game_obj = game.Game(ai_obj, ai_obj)
        game_obj.current_score = 19
        self.assertTrue(ai_obj.roll_dice(game_obj))
        game_obj.current_score = 20
        self.assertFalse(ai_obj.roll_dice(game_obj))

    def test_hard_ai(self):
        ai_obj = ai.Ai(3)
        game_obj = game.Game(ai_obj, ai_obj)
        game_obj.current_score = 19
        self.assertTrue(ai_obj.roll_dice(game_obj))
        game_obj.current_score = 30
        self.assertFalse(ai_obj.roll_dice(game_obj))

    def test_easy_ai(self):
        ai_obj = ai.Ai(1)
        ai_obj.ran.seed(7)
        self.assertFalse(ai_obj.roll_dice(2))
        self.assertTrue(ai_obj.roll_dice(2))
