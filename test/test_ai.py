# TODO: test ai implementation
import unittest
from Pig import ai

"""Unit test."""

class test_ai(unittest.TestCase):
    """test ai class."""
    def test_init(self):
        """initiates object and checks propertis."""
        res = ai.Ai(1)
        exp = ai.Ai
        self.assertIsInstance(exp, res)
        self.assertIsInstance(None, res.perfect_play)
    
    def test_select_dificulty_1(self):
        """initiates difficulty to easy and checks function return/name."""
        ai_obj = ai.Ai(1)
        res = ai_obj.select_dificulty(1).__name__
        exp = "simple"
        self.assertEqual(exp, res)
        self.assertEqual('pig-let', ai_obj.name)

    def test_select_dificulty_2(self):
        """initiates difficulty to easy and checks function return/name."""
        ai_obj = ai.Ai(2)
        res = ai_obj.select_dificulty(2).__name__
        exp = "normal"
        self.assertEqual(exp, res)
        self.assertEqual('pig', ai_obj.name)

    def test_select_dificulty_3(self):
        """initiates difficulty to easy and checks function return/name."""
        ai_obj = ai.Ai(3)
        res = ai_obj.select_dificulty(3).__name__
        exp = "hard"
        self.assertEqual(exp, res)
        self.assertEqual('Boar', ai_obj.name)

    def test_invalid_dificulty(self):
        """initiates object with invalid dificulty."""
        ai_obj = ai.Ai(2)
        res = ai_obj.select_dificulty(2).__name__
        exp = "normal"
        self.assertEqual(exp, res)
        self.assertEqual('pig', ai_obj.name)

    def test_file_not_found(self):
        """load non existing file."""
        ai_obj = ai.Ai(3)
        ai_obj.file_name = "test_file.bin"

        with self.assertRaises(FileNotFoundError):         
            ai_obj.select_dificulty(3)        
    
    def test_load_file(self):
        """load existing file."""
        ai_obj = ai.Ai(1)
        ai_obj.load_perfect_play()
        self.assertIsInstance(dict, ai_obj.perfect_play)
    
    