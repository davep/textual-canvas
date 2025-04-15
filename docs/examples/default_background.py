from textual.app import App, ComposeResult

from textual_canvas import Canvas


class DefaultBackgroundApp(App[None]):
    CSS = """
    Canvas {
        border: solid black;
        background: cornflowerblue;
    }
    """

    def compose(self) -> ComposeResult:
        yield Canvas(30, 30)  # (1)!


if __name__ == "__main__":
    DefaultBackgroundApp().run()
