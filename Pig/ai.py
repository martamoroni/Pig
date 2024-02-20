# TODO: add ai implementaion 
import pickle

"""game ai behaviour."""

class Ai():
    """ai instance."""
    def __init__(self, difficulty) -> None:
        """initiation object."""
        self.name = None        
        self.file_name = "docs/pig_perfect_play.bin"
        self.perfect_play = None
        self.roll_dice = self.select_dificulty(difficulty) 

        
    def load_perfect_play(self) -> None:
        """load the perfect play instructions."""
        with open (self.file_name, 'rb') as f:
            self.perfect_play = pickle.load(f)

    def select_dificulty(self, difficulty) -> function:
        """set name for dificulty and returns coresponding method."""
        def simple(game) -> bool:
            pass
        def normal(game) -> bool:
            pass
        def hard(game) -> bool:
            pass

        match difficulty:
            case 1:
                self.name = "pig-let"
                return simple
            case 2:
                self.name = "pig"
                return normal
            case 3:
                self.name = "Boar"
                return hard
            case _:
                print("error: not valid difficulty, difficulty set to normal")
                self.name = "pig"
                return normal



