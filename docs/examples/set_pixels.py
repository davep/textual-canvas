from textual.app import App, ComposeResult
from textual.color import Color

from textual_canvas import Canvas


class SetPixelsApp(App[None]):
    CSS = """
    Canvas {
        background: $panel;
        color: red;
    }
    """

    def compose(self) -> ComposeResult:
        yield Canvas(30, 30, Color.parse("cornflowerblue"))

    def on_mount(self) -> None:
        self.query_one(Canvas).set_pixels(
            (
                (10, 10),
                (15, 15),
                (10, 15),
                (15, 10),
            )
        )


if __name__ == "__main__":
    SetPixelsApp().run()
