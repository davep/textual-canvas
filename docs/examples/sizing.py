from textual.app import App, ComposeResult
from textual.color import Color

from textual_canvas import Canvas


class CanvasSizingApp(App[None]):
    CSS = """
    Screen {
        layout: horizontal;
    }

    Canvas {
        background: $panel;
        border: solid cornflowerblue;
        width: 1fr;
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield Canvas(20, 20, Color(128, 0, 128), id="smaller")
        yield Canvas(60, 60, Color(128, 0, 128), id="bigger")


if __name__ == "__main__":
    CanvasSizingApp().run()
