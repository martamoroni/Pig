"""High score updated and managed."""

import pickle


class ScoreBoard:
    """Score board."""

    def __init__(self) -> None:
        """Initialize the object."""
        self.players = self._load_scores("docs/high_scores.bin")

    def up_date_score(self, game) -> None:
        """Up dates the game played and won."""
        self._up_date_game_played(game.player1.name)
        self._up_date_game_played(game.player2.name)
        self._up_date_game_won(game.current_player.name)

    def _up_date_game_played(self, ply) -> None:
        """Up date games played for a player."""
        self.players[ply] = self.players.get(ply, {"wins": 0, "played": 0})
        self.players[ply]["played"] += 1

    def _up_date_game_won(self, ply) -> None:
        """Up date gamees won for a player."""
        self.players[ply] = self.players.get(ply, {"wins": 0, "played": 0})
        self.players[ply]["wins"] += 1

    def up_date_name(self, o_name, n_name) -> None:
        """Up date name in the score boared."""
        try:
            score = self.players[o_name]
            self.players[n_name] = score
            del self.players[o_name]
        except:
            print("old name does not exist")
            pass

    def name_exists(self, name):
        """Test if name is in the score boared."""
        return name in self.players

    def save_scores(self, file_name="docs/high_scores.bin") -> None:
        """Save the score to a file."""
        with open(file_name, "wb") as f:
            pickle.dump(self.players, f)

    def _load_scores(self, file_name) -> dict:
        """Load score boared from existing file or sets empty dict."""
        try:
            with open(file_name, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("cring Error no scores useing empty score board")
            return {}

    def calc_percent(self):
        """Calc win percentig."""
        player_percent = []
        longest = 0
        for player in self.players:
            longest = longest if len(player) < longest else len(player)
            wins = self.players[player]["wins"]
            played = self.players[player]["played"]
            percent = (wins / played) * 100
            player_percent.append((player, percent))

        player_percent.sort(key=lambda x: x[1], reverse=True)
        return player_percent, longest

    def __str__(self) -> str:
        """Display the current score boared."""
        player_percent, longest = self.calc_percent()
        score_boared = f"{'Name':<{longest+3}}{'Wins':>7}"
        score_boared += f"{'Played':>7}{'Percent':>11}\n"
        i = 1
        for tub in player_percent:
            wins = self.players[tub[0]]["wins"]
            played = self.players[tub[0]]["played"]
            score_boared += f"{i}: {tub[0]:<{longest}}{wins:>7}"
            score_boared += f"{played:>7}{tub[1]:>10.0f}%\n"
            i += 1
        return score_boared
