from textual.app import App, ComposeResult
from textual.color import Color

from textual_canvas import Canvas


class SetPixelApp(App[None]):
    CSS = """
    Canvas {
        background: $panel;
    }
    """

    def compose(self) -> ComposeResult:
        yield Canvas(30, 30, Color.parse("cornflowerblue"))

    def on_mount(self) -> None:
        for offset, colour in enumerate(("red", "green", "blue")):
            self.query_one(Canvas).set_pixel(
                10 + offset,
                10 + offset,
                Color.parse(colour),
            )


if __name__ == "__main__":
    SetPixelApp().run()
