# TODO: what data should be tracked, right now only played and won
# TODO: how should boared be displayed
"""high score updated and managed."""
import pickle


class ScoreBoared:
    """score boared."""

    def __init__(self) -> None:
        """init the object."""
        self.file_name = "docs/high_scores.bin"
        self.players = self._load_scores(self.file_name)

    def up_date_score(self, game) -> None:
        """up dates the game played and won."""
        self._up_date_game_played(game.player1.name)
        self._up_date_game_played(game.player2.name)
        self._up_date_game_won(game.current_player.name)

    def _up_date_game_played(self, player) -> None:
        """up date games played for a player."""
        self.players[player] = self.players.get(player, {"wins": 0, "played": 0})
        self.players[player]["played"] += 1

    def _up_date_game_won(self, player) -> None:
        """up date gamees won for a player."""
        self.players[player] = self.players.get(player, {"wins": 0, "played": 0})
        self.players[player]["wins"] += 1

    def up_date_name(self, old_name, new_name) -> None:
        """up date name in the score boared."""
        self.players[new_name] = self.players[old_name]
        del self.players[old_name]

    def name_exists(self, name):
        """test if name is in the score boared."""
        return name in self.players

    def save_scores(self, file_name) -> None:
        """save the score to a file."""
        with open(file_name, "wb") as f:
            pickle.dump(self.players, f)

    def _load_scores(self, file_name) -> dict:
        """loads score boared from existing file or sets empty dict."""
        try:
            with open(file_name, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("cring Error no scores useing empty score board")
            return {}

    def __str__(self) -> str:
        """to string method for score boared."""
        return "test"
