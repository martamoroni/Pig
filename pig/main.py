"""Module that defines the main class."""

import os
import sys
this_dir = os.path.dirname(os.path.abspath(__file__))
proj_dir = os.path.abspath(os.path.join(this_dir, ".."))
sys.path.append(proj_dir)
import ui


def main():
    """Start user interface."""
    ui2 = ui.Ui()
    ui2.cmdloop()


if __name__ == "__main__":
    main()
