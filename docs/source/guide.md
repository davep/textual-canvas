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

When [creating it][textual_canvas.canvas.Canvas] you provide a
width and a height of the canvas in "pixels" Note that these values are the
dimensions of the canvas that the "pixels" are drawn on, not the size of the
widget; the widget itself is sized using all the normal Textual styling and
geometry rules.

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

By default the canvas background colour will be set to the widget's
background colour; but you can pass
[`canvas_color`][textual_canvas.canvas.Canvas] as a parameter to change
this.

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

!!! note

    The defaulting of the canvas background to the widget's background is
    something that only happens when the widget is mounted. If you style the
    widget's background differently later on, the canvas' background **will
    not change accordingly**.

#### The pen colour

The `Canvas` widget has a "pen" colour; any time a drawing operation is
performed, if no colour is given to the method, the "pen" colour is used. By
default that colour is taken from the
[`color`](https://textual.textualize.io/styles/color/) styling of the
widget.

!!! note

    The defaulting of the pen colour to the widget's colour is
    something that only happens when the widget is mounted. If you style the
    widget's `color` differently later on, the canvas' pen colour **will
    not change accordingly**.

[//]: # (guide.md ends here)
