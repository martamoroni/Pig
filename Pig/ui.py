import cmd

class Ui(cmd.Cmd):
    prompt = "(Game) > "

    # menu to show when it starts running

    # menu after the start
    # plus start game

    # menu if choses AI

    def do_quit(self, argv):
        """This exits the program"""
        return True
    
    #aliasing
    do_exit = do_quit