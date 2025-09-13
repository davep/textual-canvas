"""Snapshot test the core plotting methods."""

##############################################################################
# Python imports.
from typing import Any, Callable

##############################################################################
# Textual imports.
from textual.app import App, ComposeResult
from textual.color import Color

##############################################################################
# Local imports.
from textual_canvas import Canvas

##############################################################################
# Helpful constants.
UNSET = Color(0, 0, 0)
SET = Color(255, 255, 255)


##############################################################################
class CanvasApp(App[None]):
    """Base application for Canvas tests."""

    def compose(self) -> ComposeResult:
        yield Canvas(100, 100, UNSET)


##############################################################################
def test_untouched(snap_compare: Callable[[Any], bool]) -> None:
    """Snapshot test for an untouched canvas."""

    assert snap_compare(CanvasApp())


##############################################################################
def test_pixel(snap_compare: Callable[[Any], bool]) -> None:
    """Snapshot test for plotting a single pixel."""

    class PixelApp(CanvasApp):
        def on_mount(self) -> None:
            self.query_one(Canvas).set_pixel(0, 0, SET)

    assert snap_compare(PixelApp())


##############################################################################
def test_line(snap_compare: Callable[[Any], bool]) -> None:
    """Snapshot test for plotting a line."""

    class LineApp(CanvasApp):
        def on_mount(self) -> None:
            self.query_one(Canvas).draw_line(0, 0, 20, 20, SET)

    assert snap_compare(LineApp())


##############################################################################
def test_tiny_line(snap_compare: Callable[[Any], bool]) -> None:
    """Snapshot test for plotting a line."""

    class TinyLineApp(CanvasApp):
        def on_mount(self) -> None:
            self.query_one(Canvas).draw_line(0, 0, 0, 1, SET)

    assert snap_compare(TinyLineApp())


##############################################################################
def test_very_tiny_line(snap_compare: Callable[[Any], bool]) -> None:
    """Snapshot test for plotting a line."""

    class VeryTinyLineApp(CanvasApp):
        def on_mount(self) -> None:
            self.query_one(Canvas).draw_line(0, 0, 0, 0, SET)

    assert snap_compare(VeryTinyLineApp())


##############################################################################
def test_rectangle(snap_compare: Callable[[Any], bool]) -> None:
    """Snapshot test for plotting a rectangle."""

    class RectangleApp(CanvasApp):
        def on_mount(self) -> None:
            self.query_one(Canvas).draw_rectangle(0, 0, 20, 20, SET)

    assert snap_compare(RectangleApp())


##############################################################################
def test_tiny_rectangle(snap_compare: Callable[[Any], bool]) -> None:
    """Snapshot test for plotting a tiny rectangle."""

    class TinyRectangleApp(CanvasApp):
        def on_mount(self) -> None:
            self.query_one(Canvas).draw_rectangle(0, 0, 1, 1, SET)

    assert snap_compare(TinyRectangleApp())


##############################################################################
def test_very_tiny_rectangle(snap_compare: Callable[[Any], bool]) -> None:
    """Snapshot test for plotting a very tiny rectangle."""

    class VeryTinyRectangleApp(CanvasApp):
        def on_mount(self) -> None:
            self.query_one(Canvas).draw_rectangle(0, 0, 0, 0, SET)

    assert snap_compare(VeryTinyRectangleApp())


##############################################################################
def test_circle(snap_compare: Callable[[Any], bool]) -> None:
    """Snapshot test for plotting a circle."""

    class CircleApp(CanvasApp):
        def on_mount(self) -> None:
            self.query_one(Canvas).draw_circle(20, 20, 5, SET)

    assert snap_compare(CircleApp())


### test_plots.py ends here
