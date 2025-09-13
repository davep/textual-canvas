"""Snapshot test for setting the pen colour."""

##############################################################################
# Python imports.
from typing import Callable

##############################################################################
# Textual imports.
from textual.app import App, ComposeResult
from textual.color import Color

##############################################################################
# Local imports.
from textual_canvas import Canvas


##############################################################################
def test_pen_colour(snap_compare: Callable[..., bool]) -> None:
    """Snapshot test setting the pen colour."""

    class PenApp(App[None]):
        def compose(self) -> ComposeResult:
            yield Canvas(20, 20)

        def on_mount(self) -> None:
            canvas = self.query_one(Canvas)
            canvas.set_pixel(0, 0)
            canvas.set_pen(Color(255, 0, 0))
            canvas.set_pixel(1, 0)
            canvas.set_pen(None)
            canvas.set_pixel(2, 0)

    assert snap_compare(PenApp())


### test_pen_color.py ends here
