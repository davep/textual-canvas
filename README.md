# textual-canvas

![Being used for textual-mandelbrot](https://raw.githubusercontent.com/davep/textual-canvas/main/img/textual-mandelbrot.png)
*An example of `textual-canvas` being used in a Textual application*

## Introduction

This library aims to provide a very simple terminal-based drawing canvas
widget for use with [Textual](https://textual.textualize.io/). Initially
developed for a (also-being-worked-on-right-now) less general project, I'm
making it available on the off-chance anyone else might want to play with it
now.

You might not want to rely on this just yet though; I'm still messing and
experimenting.

## Installing

The package can be installed with `pip` or related tools, for example:

```sh
$ pip install textual-canvas
```

## The library

The library provides one very simple widget for use in Textual: `Canvas`.
This is a scrollable and focusable widget that can be used to colour
"pixels", acting as a basic building block for drawing other things. The
"pixels" themselves are half a character cell in height, hopefully coming
out roughly square in most environments.

The `Canvas` can be imported like this:

```python
from textual_canvas import Canvas
```

And is created by providing a width and height (in its own idea of "pixels")
plus an optional initial background colour (which should be a Textual
[`Color`](https://textual.textualize.io/api/color/#textual.color.Color)).

In a Textual `compose` method you might use it something like this:

```python
yield Canvas(120, 120, Color(30, 40, 50))
```

Currently there are the following methods available for drawing:

- `clear(self, color: Color | None = None) -> Self`
- `set_pixel(self, x: int, y: int, color: Color) -> Self`
- `set_pixels(self, locations: Iterable[ tuple[ int, int ] ], color: Color) -> Self`
- `draw_line(self, x0: int, y0: int, x1: int, y1: int, color: Color) -> Self`
- `draw_rectangle(self, x: int, y: int, width: int, height: int, color: Color) -> Self`
- `draw_circle(self, center_x: int, center_y: int, radius: int, color: Color) -> Self`

I'll document all of this better, when I spend more time on it than the 1/2
hour somewhere between dinner and bedtime.

A quick and dirty example of this being used would be:

```python
from textual.app import App, ComposeResult
from textual.color import Color
from textual_canvas import Canvas


##############################################################################
class CanvasTestApp(App[None]):
    """The Canvas testing application."""

    CSS = """
    Canvas {
        border: round green;
        width: 1fr;
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield Canvas(120, 120, Color(30, 40, 50))

    def on_mount(self) -> None:
        """Set up the display once the DOM is available."""
        canvas = self.query_one(Canvas)

        canvas.draw_line(60, 40, 90, 80, Color(128, 128, 128))
        canvas.draw_line(60, 40, 30, 80, Color(128, 128, 128))
        canvas.draw_line(30, 80, 90, 80, Color(128, 128, 128))

        canvas.draw_line(0, 70, 48, 55, Color(255, 255, 255))

        for n in range(52, 59):
            canvas.draw_line(48, 55, 58, n, Color(128, 128, 128))

        canvas.draw_line(70, 52, 119, 57, Color(255, 0, 0))
        canvas.draw_line(71, 53, 119, 58, Color(255, 165, 0))
        canvas.draw_line(72, 54, 119, 59, Color(255, 255, 0))
        canvas.draw_line(72, 55, 119, 60, Color(0, 255, 0))
        canvas.draw_line(73, 56, 119, 61, Color(0, 0, 255))
        canvas.draw_line(74, 57, 119, 62, Color(75, 0, 130))
        canvas.draw_line(75, 58, 119, 63, Color(143, 0, 255))


if __name__ == "__main__":
    CanvasTestApp().run()
```

To see this code in action you, in an environment where the library is
installed, run:

```sh
$ python -m textual_canvas
```

You should see something like this:

![Demo code](https://raw.githubusercontent.com/davep/textual-canvas/main/img/textual-canvas.png)

## TODO

Lots. Lots and lots. As mentioned above, there's little tinker project that
I'm building on top of this, so I'll be using that to see how this gets
fleshed out.

[//]: # (README.md ends here)
