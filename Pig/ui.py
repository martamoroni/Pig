# change things from cmd to normal user input 

import cmd

class Ui(cmd.Cmd):
    def __init__(self) -> None:
        self.prompt = "(Game) > "
        self.completekey = "tab"
        self.cmdqueue = []

        self.in_menu = False
        self.in_start = False
        self.in_difficulty = False

        self.initialization_menu()


    def initialization_menu(self):
        print("\nWelcome to PIG!")
        self.do_MENU(self)


    def do_MENU(self, argv):
        print("\n----- MENU -----")
        print("1. Start") # New game
        print("2. ContinueGame")
        print("3. Board")
        print("4. ChangeName")
        print("5. Rules")
        print("6. Exit\n")
        self.in_menu = True

    
    def do_Start(self, argv):
        if self.in_menu:
            print("\nChoose game type:\n")
            print("1. 1VS1")
            print("2. 1VSAI")
            print("MENU")
            self.in_menu = False
            self.in_start = True
        else:
            print("Select option from current menu")


    def do_1VS1(self, argv):
        pass


    def do_1VSAI(self, argv):
        if self.in_start:
            print("\nChoose difficulty:\n")
            print("1. Piglet")
            print("2. Pig")
            print("3. Boar")
            print("4. MENU")
            self.in_start = False
            self.in_start = True

    
    def do_Piglet(self, argv):
        pass


    def do_Pig(self, argv):
        pass


    def do_Boar(self, argv):
        pass


    def do_ContinueGame(self, argv):
        pass

    def do_Board(self, argv):
        pass

    def do_ChangeName(self, argv):
        pass

    def do_Rules(self, argv):
        pass

    def do_Exit(self, argv):
        """This exits the program"""
        if self.in_menu:
            return True
        else:
            print("Select option from current menu")
    
    
    #aliasing
    do_menu = do_MENU