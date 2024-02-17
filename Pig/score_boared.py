# TODO: what data should be tracked, right now only played and won
# TODO: how should boared be displayed 
import pickle
class ScoreBoared():
    
    def __init__(self) -> None:
        players = dict()
        file_name = "high_scores.bin"
        self.loade_scores(file_name)
    
    def up_date_score(self, game) -> None:
        self.up_date_game_played(game.player1.name)
        self.up_date_game_played(game.player2.name)
        self.up_date_game_won(game.current_player.name)

    def up_date_game_played(self, player) -> None:
        self.players[player] = self.players.get(player, {"wins":0, "played":0})
        self.players[player]["played"] += 1
        
    def up_date_game_won(self, player) -> None:
        self.players[player] = self.players.get(player, {"wins":0, "played":0})
        self.players[player]["wins"] += 1

    def up_date_name(self, old_name, new_name) -> None:
        self.players[new_name] = self.players[old_name]
        del self.players[old_name]

    def name_exists(self, name):
        return name in self.players

    def save_scores(self) -> None:
        with open("high_scores.bin", "wb") as f:
            pickle.dump(self.players, f)

    def load_scores(self, file_name) -> None:
        try:
            with open(file_name, "rb") as f:
                self.players = pickle.load(f)
        except FileNotFoundError:
            print("cring Error no scores useing empty score board")
            
    def __str__(self) -> str:
        return "test"
    
