from textual.app import App, ComposeResult
from textual.color import Color

from textual_canvas import Canvas


class ClearPixelApp(App[None]):
    CSS = """
    Canvas {
        background: $panel;
        color: blue;
    }
    """

    def compose(self) -> ComposeResult:
        yield Canvas(30, 30, Color.parse("cornflowerblue"))

    def on_mount(self) -> None:
        self.query_one(Canvas).draw_line(10, 10, 15, 10).clear_pixel(12, 10)


if __name__ == "__main__":
    ClearPixelApp().run()
