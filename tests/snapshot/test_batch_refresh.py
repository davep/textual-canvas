"""Snapshot test for plotting inside a batch refresh."""

##############################################################################
# Python imports.
from collections.abc import Callable

##############################################################################
# Textual imports.
from textual.app import App, ComposeResult

##############################################################################
# Local imports.
from textual_canvas import Canvas


##############################################################################
def test_batch_refresh(snap_compare: Callable[..., bool]) -> None:
    """Snapshot test for plotting inside a batch refresh."""

    class BatchApp(App[None]):
        def compose(self) -> ComposeResult:
            yield Canvas(20, 20)

        def on_mount(self) -> None:
            with (canvas := self.query_one(Canvas)).batch_refresh():
                canvas.set_pixel(0, 0)
                canvas.set_pixel(1, 1)
                canvas.set_pixel(1, 0)
                canvas.set_pixel(0, 1)

    assert snap_compare(BatchApp())


### test_batch_refresh.py ends here
