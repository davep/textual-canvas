from textual.app import App, ComposeResult
from textual.color import Color

from textual_canvas import Canvas


class SetPixelApp(App[None]):
    CSS = """
    Canvas {
        background: $panel;
        color: red;
    }
    """

    def compose(self) -> ComposeResult:
        yield Canvas(30, 30, Color.parse("cornflowerblue"))

    def on_mount(self) -> None:
        self.query_one(Canvas).set_pixel(10, 10)


if __name__ == "__main__":
    SetPixelApp().run()
