# textual-canvas ChangeLog

## Unreleased

**Released: WiP**

- Migrated from `rye` to `uv` for development management.
- Added Python 3.14 as a tested/supported Python version.

## v0.4.0

**Released: 2025-04-16**

- Added `width` and `height` parameters to `Canvas.clear`.
  ([#17](https://github.com/davep/textual-canvas/pull/17))

## v0.3.0

**Released: 2025-04-15**

- Renamed `color` `__init__` parameter to `canvas_color`.
  ([#7](https://github.com/davep/textual-canvas/pull/7))
- Added `pen_color` as an `__init__` parameter; defaults to the widget's
  currently-styled `color`.
  ([#7](https://github.com/davep/textual-canvas/pull/7))
- Made the "void"'s colour the widget's styled background colour.
  ([#7](https://github.com/davep/textual-canvas/pull/7))
- Made the canvas colour optional; defaulting to the widget's
  currently-styled background colour.
  ([#7](https://github.com/davep/textual-canvas/pull/7))
- Made all `color` parameters for drawing methods optional, defaulting to
  the current "pen colour". ([#7](https://github.com/davep/textual-canvas/pull/7))
- Added `set_pen`. ([#7](https://github.com/davep/textual-canvas/pull/7))
- Fixed off-by-one issue with `draw_rectangle`.
  ([#10](https://github.com/davep/textual-canvas/pull/10))
- Added `Canvas.clear_pixels`.
  ([#11](https://github.com/davep/textual-canvas/pull/11))
- Added `Canvas.clear_pixel`.
  ([#11](https://github.com/davep/textual-canvas/pull/11))
- Added an optional `refresh` parameter to all drawing methods.
- Added a `Canvas.batch_refresh` context manager.

## v0.2.0

**Released: 2023-07-16**

- Dropped Python 3.7 as a supported Python version.
- Added `Canvas.clear`

## v0.1.0

**Released: 2023-04-01**

- Allow for drawing shapes partially off the canvas.
- Added support for drawing circles.

## v0.0.1

**Released: 2023-03-27**

Initial release.

[//]: # (ChangeLog.md ends here)
