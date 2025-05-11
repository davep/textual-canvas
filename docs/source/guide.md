# Usage Guide

## The `Canvas` widget

The [`Canvas`][textual_canvas.canvas.Canvas] widget is used like any other
Textual widget; it is imported as:

```python
from textual_canvas import Canvas
```

and then can be [mounted][textual.screen.Screen.mount] or
[composed][textual.screen.Screen.compose] like any other widget.

### Sizing

When [creating it][textual_canvas.canvas.Canvas] you provide a width and a
height of the canvas in "pixels". Note that these values are the dimensions
of the canvas that the "pixels" are drawn on, not the size of the widget;
the widget itself is sized using all the [normal Textual styling and
geometry rules](https://textual.textualize.io/guide/layout/).

To illustrate, here are two `Canvas` widgets, one where the widget is bigger
than the canvas, and one where the canvas is bigger than the widget:

=== "Widget vs canvas sizing"

    ```{.textual path="docs/examples/sizing.py" lines=20 columns=80}
    ```

=== "sizing.py"

    ```python
    --8<-- "docs/examples/sizing.py"
    ```

Note how the `Canvas` widget on the left is bigger than the canvas it is
displaying; whereas the widget on the right is smaller than its canvas so it
has scrollbars.

### Colours

There are three main colours to consider when working with `Canvas`:

- The widget background colour.
- The canvas background colour.
- The current "pen" colour.

#### Widget vs canvas background

The difference ion the first two items listed above might not seem obvious
to start with. The `Canvas` widget, like all other Textual widgets, has a
[background](https://textual.textualize.io/styles/background/); you can
style this with CSS just as you always would. But the canvas itself -- the
area that you'll be drawing in inside the widget -- can have its own
background colour.

By default the canvas background colour will be the widget's background
colour; but you can pass [`canvas_color`][textual_canvas.canvas.Canvas] as a
parameter to change this.

To illustrate, here is a `Canvas` widget where no background colour is
specified, so the canvas background and the widget background are the same:

=== "30x30 canvas with widget's background"

    ```{.textual path="docs/examples/default_background.py"}
    ```

=== "default_background.py"

    ```python
    --8<-- "docs/examples/default_background.py"
    ```

    1. The `Canvas` is created without a given colour, so the widget's
       `background` will be used as the canvas background colour.

Note how the user won't be able to see what's canvas background and what's
widget outside of the background.

On the other hand, if we take the same code and give the `Canvas` its own
background colour when we create it:

=== "30x30 canvas with its own background"

    ```{.textual path="docs/examples/own_background.py"}
    ```

=== "own_background.py"

    ```python hl_lines="16"
    --8<-- "docs/examples/own_background.py"
    ```

    1. Note how `Canvas` is given its own background colour.

#### The pen colour

The `Canvas` widget has a "pen" colour; any time a drawing operation is
performed, if no colour is given to the method, the "pen" colour is used. By
default that colour is taken from the
[`color`](https://textual.textualize.io/styles/color/) styling of the
widget.

## Drawing on the canvas

The canvas widget provides a number of methods for drawing on it.

!!! note

    All coordinates used when drawing are relative to the top left corner of
    the canvas.

### Drawing a single pixel

Use [`set_pixel`][textual_canvas.canvas.Canvas.set_pixel] to set the colour
of a single pixel on the canvas. For example:

=== "Drawing a single pixel"

    ```{.textual path="docs/examples/set_pixel.py"}
    ```

=== "set_pixel.py"

    ```python
    --8<-- "docs/examples/set_pixel.py"
    ```

That example is using the default pen colour, which in turn is defaulting
the widget's [`color`](https://textual.textualize.io/styles/color/). Instead
we can set pixels to specific colours:

=== "Drawing pixels with specific colours"

    ```{.textual path="docs/examples/set_pixel_colour.py"}
    ```

=== "set_pixel_colour.py"

    ```python
    --8<-- "docs/examples/set_pixel_colour.py"
    ```
### Drawing multiple pixels

Use [`set_pixels`][textual_canvas.canvas.Canvas.set_pixels] to draw multiple
pixels of the same colour at once. For example:

=== "Drawing multiple pixels"

    ```{.textual path="docs/examples/set_pixels.py"}
    ```

=== "set_pixels.py"

    ```python
    --8<-- "docs/examples/set_pixels.py"
    ```

### Drawing a line

Use [`draw_line`][textual_canvas.canvas.Canvas.draw_line] to draw a line on
the canvas. For example:

=== "Drawing a line"

    ```{.textual path="docs/examples/draw_line.py"}
    ```

=== "draw_line.py"

    ```python
    --8<-- "docs/examples/draw_line.py"
    ```

### Drawing a rectangle

Use [`draw_rectangle`][textual_canvas.canvas.Canvas.draw_rectangle] to draw
a rectangle on the canvas. For example:

=== "Drawing a rectangle"

    ```{.textual path="docs/examples/draw_rectangle.py"}
    ```

=== "draw_rectangle.py"

    ```python
    --8<-- "docs/examples/draw_rectangle.py"
    ```

### Drawing a circle

Use [`draw_circle`][textual_canvas.canvas.Canvas.draw_circle] to draw a
circle on the canvas. For example:

=== "Drawing a circle"

    ```{.textual path="docs/examples/draw_circle.py"}
    ```

=== "draw_circle.py"

    ```python
    --8<-- "docs/examples/draw_circle.py"
    ```

### Clearing a single pixel

Use [`clear_pixel`][textual_canvas.Canvas.clear_pixel] to set a pixel's
colour to the canvas' colour. For example:

=== "Clearing a single pixel"

    ```{.textual path="docs/examples/clear_pixel.py"}
    ```

=== "clear_pixel.py"

    ```python
    --8<-- "docs/examples/clear_pixel.py"
    ```

### Clearing multiple pixels

Use [`clear_pixels`][textual_canvas.Canvas.clear_pixels] to set the colour
of multiple pixels to the canvas' colour. For example:

=== "Clearing multiple pixels"

    ```{.textual path="docs/examples/clear_pixels.py"}
    ```

=== "clear_pixels.py"

    ```python
    --8<-- "docs/examples/clear_pixels.py"
    ```

## Further help

You can find more detailed documentation of the API [in the next
section](canvas.md). If you still have questions or have ideas for
improvements please feel free to chat to me [in GitHub
discussions](https://github.com/davep/textual-canvas/discussions); if you
think you've found a problem, please feel free to [raise an
issue](https://github.com/davep/textual-canvas/issues).

[//]: # (guide.md ends here)
