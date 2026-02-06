from collections.abc import Iterator

from textual.app import App, ComposeResult
from textual.color import Color

from textual_canvas.canvas import Canvas

BLUE_BROWN = [
    Color(66, 30, 15),
    Color(25, 7, 26),
    Color(9, 1, 47),
    Color(4, 4, 73),
    Color(0, 7, 100),
    Color(12, 44, 138),
    Color(24, 82, 177),
    Color(57, 125, 209),
    Color(134, 181, 229),
    Color(211, 236, 248),
    Color(241, 233, 191),
    Color(248, 201, 95),
    Color(255, 170, 0),
    Color(204, 128, 0),
    Color(153, 87, 0),
    Color(106, 52, 3),
]
"""https://stackoverflow.com/a/16505538/2123348"""


def mandelbrot(x: float, y: float) -> int:
    c1 = complex(x, y)
    c2 = 0j
    for n in range(40):
        if abs(c2) > 2:
            return n
        c2 = c1 + (c2**2.0)
    return 0


def frange(r_from: float, r_to: float, size: int) -> Iterator[tuple[int, float]]:
    steps = 0
    step = (r_to - r_from) / size
    n = r_from
    while n < r_to and steps < size:
        yield steps, n
        n += step
        steps += 1


class MandelbrotApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Canvas(120, 90)

    def on_mount(self) -> None:
        with (canvas := self.query_one(Canvas)).batch_refresh():
            for x_pixel, x_point in frange(-2.5, 1.5, canvas.width):
                for y_pixel, y_point in frange(-1.5, 1.5, canvas.height):
                    canvas.set_pixel(
                        x_pixel,
                        y_pixel,
                        BLUE_BROWN[value % 16]
                        if (value := mandelbrot(x_point, y_point))
                        else Color(0, 0, 0),
                    )


if __name__ == "__main__":
    MandelbrotApp().run()
