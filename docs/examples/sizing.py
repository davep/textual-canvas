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

    def on_mount(self) -> None:
        self.query_one("#smaller").border_title = "Widget > Canvas"
        self.query_one("#bigger").border_title = "Canvas > Widget"


if __name__ == "__main__":
    CanvasSizingApp().run()
