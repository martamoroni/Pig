class Ai():
    def __init__(self, difficulty) -> None:
        self.name = ""        
        self.behaviour = self.select_dificulty(difficulty) 

    def roll_dice(self) -> bool:
        return self.behaviour():
        
    def select_dificulty(self, difficulty) -> function:
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


