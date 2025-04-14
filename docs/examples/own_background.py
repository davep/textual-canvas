from textual.app import App, ComposeResult
from textual.color import Color

from textual_canvas import Canvas


class OwnBackgroundApp(App[None]):
    CSS = """
    Canvas {
        border: solid black;
        background: cornflowerblue;
    }
    """

    def compose(self) -> ComposeResult:
        yield Canvas(30, 30, Color(80, 80, 255))  # (1)!


if __name__ == "__main__":
    OwnBackgroundApp().run()
