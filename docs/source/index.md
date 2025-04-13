# Introduction

`textual-canvas` provides a simple terminal-based drawing canvas widget for
use with [Textual](https://textual.textualize.io/). Initially developed as a
widget for building
[`textual-mandelbrot`](https://github.com/davep/textual-mandelbrot), it made
sense to spin it out into its own general-purpose library.

=== "Textual Canvas Example"

    ```{.textual path="docs/examples/prism.py" lines=62 columns=122}
    ```

=== "prism.py"

    ```py
    --8<-- "docs/examples/prism.py"
    ```

The widget is based around the use of half block characters; this has two
main advantages:

- The "pixels" are generally nice and square in most terminal setups.
- You get to use the [full range of
  colours](https://textual.textualize.io/api/color/) for each pixel.

[//]: # (index.md ends here)
