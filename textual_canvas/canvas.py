"""Provides a simple character cell-based canvas widget for Textual applications."""

##############################################################################
# Python imports.
from __future__ import annotations
from functools  import lru_cache
from math       import ceil

##############################################################################
# Rich imports.
from rich.segment import Segment
from rich.style   import Style

##############################################################################
# Textual imports.
from textual.color       import Color
from textual.geometry    import Size
from textual.scroll_view import ScrollView
from textual.strip       import Strip

##############################################################################
class Canvas( ScrollView, can_focus=True ):
    """A simple character-cell canvas widget.

    The widget is designed such that there are two 'pixels' per character
    cell; one being the top half of the cell, the other being the bottom.
    While not exactly square, this will make it more square than using a
    whole cell as a simple pixel.

    The origin of the canvas is the top left corner.

    NOTE: At the moment this is coded in a very simple way, mainly to help
    decide on the API it will make available (which I intend to be as simple
    as possible). Little to no thought has been given to performance. First
    I want to get it right, then I want to get it fast.
    """

    def __init__(
        self,
        width: int,
        height: int,
        color: Color = Color( 0, 0, 0),
        name: str | None    = None,
        id: str | None      = None, # pylint:disable=redefined-builtin
        classes: str | None = None,
        disabled: bool      = False
    ):
        """Initialise the canvas.

        Args:
            width: The width of the canvas.
            height: The height of the canvas.
            color: An optional default colour for the canvas.
            name: The name of the canvas widget.
            id: The ID of the canvas widget in the DOM.
            classes: The CSS classes of the canvas widget.
            disabled: Whether the canvas widget is disabled or not.
        """
        # Pass the normal Textual widget stuff up the chain.
        super().__init__( name=name, id=id, classes=classes, disabled=disabled )

        # Remember the width and height.
        self._width  = width
        self._height = height

        # Generate the underlying "canvas" structure.
        self._canvas = [
            [ color for _ in range( width ) ] for _ in range( height )
        ]

        # Used as a source of "there's nothing here" for the last row in a
        # canvas if we're likely to go off the end.
        #
        # TODO: Rather than use the default colour of the canvas, perhaps
        # take the background color of the widget itself?
        self._the_void = [ color for _ in range( width ) ]

        # Ensure we can scroll around the canvas.
        self.virtual_size = Size( self._width, ceil( self._height / 2 ) )

    @property
    def width( self ) -> int:
        """The width of the canvas in 'pixels'."""
        return self._width

    @property
    def height( self ) -> int:
        """The height of the canvas in 'pixels'."""
        return self._height

    def set_pixel( self, x: int, y: int, color: Color ) -> None:
        """Set the colour of a specific pixel on the canvas.

        Args:
            x: The horizontal location of the pixel.
            y: The vertical location of the pixel.
            color: The color to set the pixel to.

        Note:
            The origin of the canvas is the top left corner.
        """
        self._canvas[ y ][ x ] = color
        self.refresh()

    def get_pixel( self, x: int, y: int ) -> Color:
        """Get the pixel at the given location.

        Args:
            x: The horizontal location of the pixel.
            y: The vertical location of the pixel.

        Returns:
            The colour of the pixel at that location.
        """
        return self._canvas[ y ][ x ]

    _CELL = "\u2584"
    """The character to use to draw two pixels in one cell in the canvas."""

    @lru_cache()
    def _segment_of( self, top: Color, bottom: Color ) -> Segment:
        """Construct a segment to show the two colours in one cell.

        Args:
            top: The colour for the top pixel.
            bottom: The colour for the bottom pixel.

        Returns:
            A `Segment` that will display the two pixels.
        """
        return Segment( self._CELL, style=Style.from_color( bottom.rich_color, top.rich_color ) )

    def render_line( self, y: int ) -> Strip:
        """Render a line in the display.

        Args:
            y: The line to render.

        Returns:
            A `Strip` that is the line to render.
        """

        # Get where we're scrolled to.
        scroll_x, scroll_y = self.scroll_offset

        # We're going to be drawing two lines from the canvas in one line in
        # the display. Let's work out the first line first.
        top_line = ( scroll_y + y ) * 2

        # Is this off the canvas already?
        if top_line >= self.height:
            # Yup. Don't bother drawing anything.
            return Strip( [] )

        # Now, the bottom line is easy enough to work out.
        bottom_line = top_line + 1

        # Get the pixel values for the top line.
        top_pixels = self._canvas[ top_line ]

        # It's possible that the bottom line might be in the void, so...
        bottom_pixels = self._the_void if bottom_line >= self.height else self._canvas[ bottom_line ]

        # At this point we know what colours we're going to be mashing
        # together into the terminal line we're drawing. So let's get to it.
        return Strip( [
            self._segment_of( top_pixels[ pixel ], bottom_pixels[ pixel ] )
            for pixel in range( self.width )
        ] ).crop( scroll_x, scroll_x + self.scrollable_content_region.width )

### canvas.py ends here
