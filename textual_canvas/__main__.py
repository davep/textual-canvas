"""A simple demonstration of the Canvas widget."""

##############################################################################
# Textual imports.
from textual import on
from textual.app import App, ComposeResult
from textual.events import Mount
from textual.color import Color

##############################################################################
# Local imports.
from .canvas import Canvas


##############################################################################
class CanvasTestApp(App[None]):
    """The Canvas testing application."""

    CSS = """
    Canvas {
        border: round green;
        width: 1fr;
        height: 1fr;
    }
    """

    BINDINGS = [
        ("r", "clear(255, 0, 0)"),
        ("g", "clear(0, 255, 0)"),
        ("b", "clear(0, 0, 255)"),
    ]

    def compose(self) -> ComposeResult:
        yield Canvas(120, 120, Color(30, 40, 50))

    @on(Mount)
    def its_all_dark(self) -> None:
        """Set up the display once the DOM is available."""
        canvas = self.query_one(Canvas)

        canvas.draw_line(60, 40, 90, 80, Color(128, 128, 128))
        canvas.draw_line(60, 40, 30, 80, Color(128, 128, 128))
        canvas.draw_line(30, 80, 90, 80, Color(128, 128, 128))

        canvas.draw_line(0, 70, 48, 55, Color(255, 255, 255))

        for n in range(52, 59):
            canvas.draw_line(48, 55, 58, n, Color(128, 128, 128))

        canvas.draw_line(70, 52, 119, 57, Color(255, 0, 0))
        canvas.draw_line(71, 53, 119, 58, Color(255, 165, 0))
        canvas.draw_line(72, 54, 119, 59, Color(255, 255, 0))
        canvas.draw_line(72, 55, 119, 60, Color(0, 255, 0))
        canvas.draw_line(73, 56, 119, 61, Color(0, 0, 255))
        canvas.draw_line(74, 57, 119, 62, Color(75, 0, 130))
        canvas.draw_line(75, 58, 119, 63, Color(143, 0, 255))

        canvas.focus()

    def action_clear(self, red: int, green: int, blue: int) -> None:
        """Handle the clear keyboard action."""
        self.query_one(Canvas).clear(Color(red, green, blue))
        self.its_all_dark()


if __name__ == "__main__":
    CanvasTestApp().run()

### __main__.py ends here
