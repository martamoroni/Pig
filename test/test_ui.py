"""Unit testing."""

import unittest
from pig import ui
from pig import score_board
from unittest import mock

class test_ui(unittest.TestCase):
    """Test Ui class."""
  
    def test_init(self):
        """Test initiation"""
        ui1 = ui.Ui()
        self.assertTrue(ui1.prompt =="(Game) > ")
        self.assertTrue(ui1.completekey == "tab")
        self.assertIsInstance(ui1.high_score, score_board.ScoreBoard)


    def test_changename_success(self):
        """Check if change name works with correct input"""
        ui1 = ui.Ui()
        
        ui1.high_score._up_date_game_played("Marta")
        with mock.patch("builtins.input", side_effect=["Marta", "Sven"]):
            ui1.do_changename()

            self.assertNotIn("Marta", ui1.high_score.players)
            self.assertIn("Sven", ui1.high_score.players)

    def test_changename_retry(self):
        """Check if change name works with 1 retry and then correct input"""
        ui1 = ui.Ui()
        
        ui1.high_score._up_date_game_played("ben")
        ui1.high_score._up_date_game_played("Marta")
        print("test")
        
        with mock.patch("builtins.input", side_effect=["Marta", "ben", "yes", "Sven"]):
            ui1.do_changename()

            self.assertNotIn("Marta", ui1.high_score.players)
            self.assertIn("Sven", ui1.high_score.players)

    def test_changename_wrong_no_retry(self):
        """Check if change name works with 1 retry and then correct input"""
        ui1 = ui.Ui()
        
        ui1.high_score._up_date_game_played("ben")
        ui1.high_score._up_date_game_played("Marta")
        print("test")
        
        with mock.patch("builtins.input", side_effect=["Marta", "ben", "no"]):
            ui1.do_changename()

            self.assertIn("Marta", ui1.high_score.players)
            self.assertNotIn("Sven", ui1.high_score.players)
        
    def test_changename_invalid(self):
        """Check when new name is invalid"""
        ui1 = ui.Ui()
        

        ui1.high_score._up_date_game_played("Marta")

        with mock.patch("builtins.input", side_effect=["Marta", "pig", "sven"]):
            ui1.do_changename()
            self.assertNotIn("pig", ui1.high_score.players)


