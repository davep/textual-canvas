"""A simple demonstration of the Canvas widget."""

##############################################################################
# Textual imports.
from textual.app   import App, ComposeResult
from textual.color import Color

##############################################################################
# Local imports.
from .canvas import Canvas

##############################################################################
class CanvasTestApp( App[ None ] ):
    """The Canvas testing application."""

    CSS = """
    Canvas {
        border: round green;
        width: 1fr;
        height: 1fr;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Canvas( 100, 100 )

    def on_mount( self ) -> None:
        """Set up the display once the DOM is available."""
        for column in range( 80 ):
            self.query_one( Canvas ).set_pixel( 10 + column, 0, Color( 255, 0, 0 ) )
            self.query_one( Canvas ).set_pixel( 10 + column, 1, Color( 0, 255, 0 ) )
            self.query_one( Canvas ).set_pixel( 10 + column, 2, Color( 0, 0, 255 ) )
            self.query_one( Canvas ).set_pixel( 10 + column, 3, Color( 128, 0, 0 ) )
            self.query_one( Canvas ).set_pixel( 10 + column, 4, Color( 0, 128, 0 ) )
            self.query_one( Canvas ).set_pixel( 10 + column, 5, Color( 0, 0, 128 ) )

            self.query_one( Canvas ).set_pixel( 10 + column, 20, Color( 255, 0, 0 ) )
            self.query_one( Canvas ).set_pixel( 10 + column, 21, Color( 0, 255, 0 ) )
            self.query_one( Canvas ).set_pixel( 10 + column, 22, Color( 0, 0, 255 ) )

if __name__ == "__main__":
    CanvasTestApp().run()

### __main__.py ends here
