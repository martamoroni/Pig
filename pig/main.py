"""Module that defines the main class."""

import fix_path
import ui


def main():
    """Start user interface."""
    ui2 = ui.Ui()
    ui2.cmdloop()
    fix_path.cry()


if __name__ == "__main__":
    main()
