"""Set Python Path."""

import os
import sys

this_dir = os.path.dirname(os.path.abspath(__file__))
proj_dir = os.path.abspath(os.path.join(this_dir, ".."))
sys.path.append(proj_dir)


def cry():
    """Stop crying."""
