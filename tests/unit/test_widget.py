"""Test the main API of the Canvas widget."""

##############################################################################
# Pytest imports.
from pytest import raises

##############################################################################
# Textual imports.
from textual.app import App, ComposeResult
from textual.color import Color

##############################################################################
# Local imports.
from textual_canvas import Canvas, CanvasError

##############################################################################
# Helpful constants.
UNSET = Color(0, 0, 0)
SET = Color(255, 255, 255)
WIDTH = 10
HEIGHT = WIDTH + 1


##############################################################################
class CanvasApp(App[None]):
    """The application for these tests."""

    def compose(self) -> ComposeResult:
        yield Canvas(WIDTH, HEIGHT, UNSET)


##############################################################################
async def test_width() -> None:
    """The canvas' width should report as what was set."""

    async with CanvasApp().run_test() as pilot:
        assert pilot.app.query_one(Canvas).width == WIDTH


##############################################################################
async def test_height() -> None:
    """The canvas' height should report as what was set."""

    async with CanvasApp().run_test() as pilot:
        assert pilot.app.query_one(Canvas).height == HEIGHT


##############################################################################
async def test_set_within_canvas() -> None:
    """Setting a pixel within the canvas should cause no problems."""

    async with CanvasApp().run_test() as pilot:
        canvas = pilot.app.query_one(Canvas).set_pixel(1, 1, SET)
        assert canvas.get_pixel(0, 0) == UNSET
        assert canvas.get_pixel(1, 1) == SET
        assert canvas.get_pixel(1, 0) == UNSET
        assert canvas.get_pixel(0, 1) == UNSET


##############################################################################
async def test_set_outwith_canvas() -> None:
    """Setting a pixel outwith the canvas should raise an error."""

    async with CanvasApp().run_test() as pilot:
        with raises(CanvasError):
            pilot.app.query_one(Canvas).set_pixel(-1, -1, SET)


##############################################################################
async def test_get_outwith_canvas() -> None:
    """Getting a pixel outwith the canvas should raise an error."""

    async with CanvasApp().run_test() as pilot:
        with raises(CanvasError):
            _ = pilot.app.query_one(Canvas).get_pixel(-1, -1)


##############################################################################
async def test_clear_within_canvas() -> None:
    """Clearing a previously-set pixel within the canvas should cause no problems."""

    async with CanvasApp().run_test() as pilot:
        canvas = pilot.app.query_one(Canvas).set_pixel(1, 1, SET)
        canvas.clear_pixel(1, 1)
        assert canvas.get_pixel(1, 1) == UNSET


##############################################################################
async def test_clear_outwith_canvas() -> None:
    """Clearing a outwith the canvas should raise an error."""

    async with CanvasApp().run_test() as pilot:
        with raises(CanvasError):
            pilot.app.query_one(Canvas).clear_pixel(-1, -1)


##############################################################################
async def test_draw_line_outwith_canvas() -> None:
    """Drawing a line outwith the canvas should cause no problems."""

    async with CanvasApp().run_test() as pilot:
        canvas = pilot.app.query_one(Canvas).draw_line(
            -WIDTH, -WIDTH, WIDTH + WIDTH, WIDTH + WIDTH, SET
        )
        assert canvas.get_pixel(1, 1) == SET


### test_widget.py ends here
