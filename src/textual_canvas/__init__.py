"""A library that provides a simple canvas for drawing in Textual."""

##############################################################################
# Python imports.
from importlib.metadata import version

######################################################################
# Main app information.
__author__ = "Dave Pearson"
__copyright__ = "Copyright 2023-2025, Dave Pearson"
__credits__ = ["Dave Pearson"]
__maintainer__ = "Dave Pearson"
__email__ = "davep@davep.org"
__version__ = version("textual_canvas")
__licence__ = "MIT"

##############################################################################
# Local imports.
from .canvas import Canvas, CanvasError

##############################################################################
# Export the imports.
__all__ = ["Canvas", "CanvasError"]

### __init__.py ends here
