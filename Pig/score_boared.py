# TODO: what data should be tracked, right now only played and won
# TODO: how should boared be displayed 
import pickle
class ScoreBoared():
    
    def __init__(self) -> None:
        players = dict()
        self.loade_scores()
    
    def up_date_score(self, game) -> None:
        self.up_date_game_played(game.player1)
        self.up_date_game_played(game.player2)
        self.up_date_game_won(game.current_player)

    def up_date_game_played(self, player) -> None:
        self.players[player.name] = self.players.get(player.name, {"wins":0, "played":0})
        self.players[player.name]["played"] += 1
        
    def up_date_game_won(self, player) -> None:
        self.players[player.name]["wins"] += 1

    def up_date_name(self, old_name, new_name) -> None:
        self.players[new_name] = self.players[old_name]
        del self.players[old_name]

    def save_scores(self) -> None:
        with open("high_scores.bin", "wb") as f:
            pikle.dump(self.players, f)

    def load_scores(self) -> None:
        try:
            with open("high_scores.bin", "rb") as f:
                self.players = pikle.load(f)
        except FileNotFoundError:
            print("cring Error no scores useing empty score board")
            
    def __str__(self) -> str:
        return "test"
    
