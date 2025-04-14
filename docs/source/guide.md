# Usage Guide

## The `Canvas` widget

The [`Canvas`][textual_canvas.canvas.Canvas] widget is used like any other
Textual widget; it is imported as:

```python
from textual_canvas import Canvas
```

and then can be [mounted][textual.screen.Screen.mount] or
[composed][textual.screen.Screen.compose] like any other widget.

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

    ```py
    --8<-- "docs/examples/sizing.py"
    ```

Note how the `Canvas` widget on the left is bigger than the canvas it is
displaying; whereas the widget on the right is smaller than its canvas so it
has scrollbars.

[//]: # (guide.md ends here)
