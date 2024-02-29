"""Unit testing."""

import unittest
from pig import player
from unittest import mock

class test_player(unittest.TestCase):
    """Test Player class."""
    @mock.patch('module_under_test.input', create = True)

    def test_init(self, name) -> None:
        """Instantiate and object and check its properties."""
        player1 = player.Player("Marta")
        exp = player.Player
        self.assertIsInstance(res, exp)

        res = player1.name
        exp = "Marta"
        self.assertEqual(res, exp)

        res = player1.points
        exp = 0
        self.assertEqual(res, exp)

    def test_roll_dice(self, game) -> bool:
        """Check if player wants to roll the dice, return True or False."""
        valid_choice = False
        print(game.current_score)
        while not valid_choice:
            choice = input("Do you want to roll the dice? (yes/no)").lower()
            choice = choice[0]
            if choice == "yes":
                return True
            elif choice == "no":
                return False
            elif choice == "cheat":
                self.points = 90
                return True
            elif choice == "exit":
                game.game_paused = True
                return False
            else:
                print("Please enter valid choice: 'yes' or 'no'")

    def test_change_name(self, mocked_input):
        """Change player name and check if change is made."""
        player1 = player.Player("Marta")

        mocked_input.return_value = "Sven"
        player1.change_name()
        self.assertEqual(player1.name, "Sven")
