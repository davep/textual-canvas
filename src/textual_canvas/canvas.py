"""Provides a simple character cell-based canvas widget for Textual applications."""

##############################################################################
# Backward compatibility.
from __future__ import annotations

##############################################################################
# Python imports.
from contextlib import contextmanager
from functools import lru_cache
from math import ceil
from typing import Generator, Iterable

##############################################################################
# Rich imports.
from rich.segment import Segment
from rich.style import Style

##############################################################################
# Textual imports.
from textual.color import Color
from textual.geometry import Size
from textual.scroll_view import ScrollView
from textual.strip import Strip

##############################################################################
# Typing extension imports.
from typing_extensions import Self


##############################################################################
class CanvasError(Exception):
    """Type of errors raised by the [`Canvas`][textual_canvas.canvas.Canvas] widget."""


##############################################################################
class Canvas(ScrollView, can_focus=True):
    """A simple character-cell canvas widget.

    The widget is designed such that there are two 'pixels' per character
    cell; one being the top half of the cell, the other being the bottom.
    While not exactly square, this will make it more square than using a
    whole cell as a simple pixel.

    The origin of the canvas is the top left corner.
    """

    def __init__(
        self,
        width: int,
        height: int,
        canvas_color: Color | None = None,
        pen_color: Color | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        disabled: bool = False,
    ):
        """Initialise the canvas.

        Args:
            width: The width of the canvas.
            height: The height of the canvas.
            canvas_color: An optional default colour for the canvas.
            pen_color: The optional default colour for the pen.
            name: The name of the canvas widget.
            id: The ID of the canvas widget in the DOM.
            classes: The CSS classes of the canvas widget.
            disabled: Whether the canvas widget is disabled or not.

        If `canvas_color` is omitted, the widget's `background` styling will
        be used.

        If `pen_color` is omitted, the widget's `color` styling will be used.
        """
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
        self._width = width
        """The widget of the canvas."""
        self._height = height
        """The height of the canvas."""
        self._canvas_colour = canvas_color
        """The background colour of the canvas itself."""
        self._pen_colour = pen_color
        """The default pen colour, used when drawing pixels."""
        self._canvas: list[list[Color | None]] = []
        """The canvas itself."""
        self._refreshing = True
        """The current default refresh state."""
        self.clear()

    @property
    def _blank_canvas(self) -> list[list[Color | None]]:
        """A blank canvas."""
        return [
            [self._canvas_colour for _ in range(self.width)] for _ in range(self.height)
        ]

    @property
    def width(self) -> int:
        """The width of the canvas in 'pixels'."""
        return self._width

    @property
    def height(self) -> int:
        """The height of the canvas in 'pixels'."""
        return self._height

    def notify_style_update(self) -> None:
        self.refresh()
        return super().notify_style_update()

    @contextmanager
    def batch_refresh(self) -> Generator[None, None, None]:
        """A context manager that suspends all calls to `refresh` until the end of the batch.

        Ordinarily [`set_pixels`][textual_canvas.canvas.Canvas.set_pixels]
        will call [`refresh`][textual.widget.Widget.refresh] once it has
        updated all of the pixels it has been given. Sometimes you may want
        to perform a number of draw operations and having `refresh` called
        between each one would be inefficient given you've not finished
        drawing yet.

        Use this context manager to batch up your drawing operations.

        Example:
            ```python
            canvas = self.query_one(Canvas)
            with canvas.batch_refresh():
                canvas.draw_line(10, 10, 10, 20)
                canvas.draw_line(10, 20, 20, 20)
                canvas.draw_line(20, 20, 20, 10)
                canvas.draw_line(20, 10, 10, 10)
            ```

        Note:
            All drawing methods have a `refresh` parameter. If that is set
            to [`True`][True] in any of your calls those calls will still
            force a refresh.
        """
        refreshing = self._refreshing
        try:
            self._refreshing = False
            yield
        finally:
            self._refreshing = refreshing
            self.refresh()

    def _outwith_the_canvas(self, x: int, y: int) -> bool:
        """Is the location outwith the canvas?

        Args:
            x: The horizontal location of the pixel.
            y: The vertical location of the pixel.

        """
        return x < 0 or y < 0 or x >= self._width or y >= self._height

    def _pixel_check(self, x: int, y: int) -> None:
        """Check that a location is within the canvas.

        Args:
            x: The horizontal location of the pixel.
            y: The vertical location of the pixel.

        Raises:
            CanvasError: If the pixel location is not within the canvas.
        """
        if self._outwith_the_canvas(x, y):
            raise CanvasError(
                f"x={x}, y={y} is not within 0, 0, {self._width}, {self._height}"
            )

    def clear(
        self,
        color: Color | None = None,
        width: int | None = None,
        height: int | None = None,
    ) -> Self:
        """Clear the canvas.

        Args:
            color: Optional default colour for the canvas.
            width: Optional width for the canvas.
            height: Optional height for the canvas.

        Returns:
            The canvas.

        If the color isn't provided, then the color used when first making
        the canvas is used, this in turn becomes the new default color (and
        will then be used for subsequent clears, unless another color is
        provided).

        Explicitly setting the colour to [`None`][None] will set the canvas
        colour to whatever the widget's `background` colour is.

        If `width` or `height` are omitted then the current value for those
        dimensions will be used.
        """
        self._width = self._width if width is None else width
        self._height = self._height if height is None else height
        self.virtual_size = Size(self._width, ceil(self._height / 2))
        self._canvas_colour = color or self._canvas_colour
        self._canvas = self._blank_canvas
        return self.refresh()

    def set_pen(self, color: Color | None) -> Self:
        """Set the default pen colour.

        Args:
            color: A colour to use by default when drawing a pixel.

        Returns:
            The canvas.

        Note:
            Setting the colour to [`None`][None] specifies that the widget's
            currently-styled [`color`](https://textual.textualize.io/guide/styles/#styles-object)
            should be used.
        """
        self._pen_colour = color
        return self

    def set_pixels(
        self,
        locations: Iterable[tuple[int, int]],
        color: Color | None = None,
        refresh: bool | None = None,
    ) -> Self:
        """Set the colour of a collection of pixels on the canvas.

        Args:
            locations: An iterable of tuples of x and y location.
            color: The color to set the pixel to.
            refresh: Should the widget be refreshed?

        Returns:
            The canvas.

        Raises:
            CanvasError: If any pixel location is not within the canvas.

        Note:
            The origin of the canvas is the top left corner.
        """
        color = color or self._pen_colour or self.styles.color
        for x, y in locations:
            self._pixel_check(x, y)
            self._canvas[y][x] = color
        if self._refreshing if refresh is None else refresh:
            self.refresh()
        return self

    def clear_pixels(
        self, locations: Iterable[tuple[int, int]], refresh: bool | None = None
    ) -> Self:
        """Clear the colour of a collection of pixels on the canvas.

        Args:
            locations: An iterable of tuples of x and y location.
            refresh: Should the widget be refreshed?

        Returns:
            The canvas.

        Raises:
            CanvasError: If any pixel location is not within the canvas.

        Note:
            The origin of the canvas is the top left corner.
        """
        return self.set_pixels(locations, self._canvas_colour, refresh)

    def set_pixel(
        self, x: int, y: int, color: Color | None = None, refresh: bool | None = None
    ) -> Self:
        """Set the colour of a specific pixel on the canvas.

        Args:
            x: The horizontal location of the pixel.
            y: The vertical location of the pixel.
            color: The color to set the pixel to.
            refresh: Should the widget be refreshed?

        Raises:
            CanvasError: If the pixel location is not within the canvas.

        Note:
            The origin of the canvas is the top left corner.
        """
        return self.set_pixels(
            ((x, y),), self._pen_colour if color is None else color, refresh
        )

    def clear_pixel(self, x: int, y: int, refresh: bool | None = None) -> Self:
        """Clear the colour of a specific pixel on the canvas.

        Args:
            x: The horizontal location of the pixel.
            y: The vertical location of the pixel.
            refresh: Should the widget be refreshed?

        Raises:
            CanvasError: If the pixel location is not within the canvas.

        Note:
            The origin of the canvas is the top left corner.
        """
        return self.clear_pixels(((x, y),), refresh)

    def get_pixel(self, x: int, y: int) -> Color:
        """Get the pixel at the given location.

        Args:
            x: The horizontal location of the pixel.
            y: The vertical location of the pixel.

        Returns:
            The colour of the pixel at that location.

        Raises:
            CanvasError: If the pixel location is not within the canvas.

        Note:
            The origin of the canvas is the top left corner.
        """
        self._pixel_check(x, y)
        return self._canvas[y][x] or self.styles.background

    def draw_line(
        self,
        x0: int,
        y0: int,
        x1: int,
        y1: int,
        color: Color | None = None,
        refresh: bool | None = None,
    ) -> Self:
        """Draw a line between two points.

        Args:
            x0: Horizontal location of the starting position.
            y0: Vertical location of the starting position.
            x1: Horizontal location of the ending position.
            y1: Vertical location of the ending position.
            color: The color to set the pixel to.
            refresh: Should the widget be refreshed?

        Returns:
            The canvas.

        Note:
            The origin of the canvas is the top left corner.
        """

        # Taken from https://en.wikipedia.org/wiki/Bresenham's_line_algorithm#All_cases.

        pixels: list[tuple[int, int]] = []

        dx = abs(x1 - x0)
        sx = 1 if x0 < x1 else -1
        dy = -abs(y1 - y0)
        sy = 1 if y0 < y1 else -1
        err = dx + dy

        while True:
            if not self._outwith_the_canvas(x0, y0):
                pixels.append((x0, y0))
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                if x0 == x1:
                    break
                err += dy
                x0 += sx
            if e2 <= dx:
                if y0 == y1:
                    break
                err += dx
                y0 += sy

        return self.set_pixels(pixels, color, refresh)

    def draw_rectangle(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: Color | None = None,
        refresh: bool | None = None,
    ) -> Self:
        """Draw a rectangle.

        Args:
            x: Horizontal location of the top left corner of the rectangle.
            y: Vertical location of the top left corner of the rectangle.
            width: The width of the rectangle.
            height: The height of the rectangle.
            color: The color to draw the rectangle in.
            refresh: Should the widget be refreshed?

        Returns:
            The canvas.

        Note:
            The origin of the canvas is the top left corner.
        """
        if width < 1 or height < 1:
            return self
        width -= 1
        height -= 1
        return (
            self.draw_line(x, y, x + width, y, color, False)
            .draw_line(x + width, y, x + width, y + height, color, False)
            .draw_line(x + width, y + height, x, y + height, color, False)
            .draw_line(x, y + height, x, y, color, refresh)
        )

    @staticmethod
    def _circle_mirror(x: int, y: int) -> tuple[tuple[int, int], ...]:
        """Create an 8-way symmetry of the given points.

        Args:
            x: Horizontal location of the point to mirror.
            y: Vertical location of the point to mirror.

        Returns:
            The points needed to create an 8-way symmetry.
        """
        return ((x, y), (y, x), (-x, y), (-y, x), (x, -y), (y, -x), (-x, -y), (-y, -x))

    def draw_circle(
        self,
        center_x: int,
        center_y: int,
        radius: int,
        color: Color | None = None,
        refresh: bool | None = None,
    ) -> Self:
        """Draw a circle

        Args:
            center_x: The horizontal position of the center of the circle.
            center_y: The vertical position of the center of the circle.
            radius: The radius of the circle.
            color: The colour to draw circle in.
            refresh: Should the widget be refreshed?

        Returns:
            The canvas.

        Note:
            The origin of the canvas is the top left corner.
        """

        # Taken from https://funloop.org/post/2021-03-15-bresenham-circle-drawing-algorithm.html.

        pixels: list[tuple[int, int]] = []

        x = 0
        y = -radius
        f_m = 1 - radius
        d_e = 3
        d_ne = -(radius << 1) + 5
        pixels.extend(self._circle_mirror(x, y))
        while x < -y:
            if f_m <= 0:
                f_m += d_e
            else:
                f_m += d_ne
                d_ne += 2
                y += 1
            d_e += 2
            d_ne += 2
            x += 1
            pixels.extend(self._circle_mirror(x, y))

        return self.set_pixels(
            [
                (center_x + x, center_y + y)
                for x, y in pixels
                if not self._outwith_the_canvas(center_x + x, center_y + y)
            ],
            color,
            refresh,
        )

    _CELL = "\u2584"
    """The character to use to draw two pixels in one cell in the canvas."""

    @lru_cache()
    def _segment_of(self, top: Color, bottom: Color) -> Segment:
        """Construct a segment to show the two colours in one cell.

        Args:
            top: The colour for the top pixel.
            bottom: The colour for the bottom pixel.

        Returns:
            A `Segment` that will display the two pixels.
        """
        return Segment(
            self._CELL, style=Style.from_color(bottom.rich_color, top.rich_color)
        )

    def render_line(self, y: int) -> Strip:
        """Render a line in the display.

        Args:
            y: The line to render.

        Returns:
            A [`Strip`][textual.strip.Strip] that is the line to render.
        """

        # Get where we're scrolled to.
        scroll_x, scroll_y = self.scroll_offset

        # We're going to be drawing two lines from the canvas in one line in
        # the display. Let's work out the first line first.
        top_line = (scroll_y + y) * 2

        # Is this off the canvas already?
        if top_line >= self.height:
            # Yup. Don't bother drawing anything.
            return Strip([])

        # Set up the two main background colours we need.
        background_colour = self.styles.background
        canvas_colour = self._canvas_colour or background_colour

        # Reduce some attribute lookups.
        height = self._height
        width = self._width
        canvas = self._canvas

        # Now, the bottom line is easy enough to work out.
        bottom_line = top_line + 1

        # Get the pixel values for the top line.
        top_pixels = canvas[top_line]

        # It's possible that the bottom line might be outwith the canvas
        # itself; so here we set the bottom line to the widget's background
        # colour if it is, otherwise we use the line form the canvas.
        bottom_pixels = (
            [background_colour for _ in range(width)]
            if bottom_line >= height
            else canvas[bottom_line]
        )

        # At this point we know what colours we're going to be mashing
        # together into the terminal line we're drawing. So let's get to it.
        # Note that in every case, if the colour we have is `None` that
        # means we're using the canvas colour.
        return (
            Strip(
                [
                    self._segment_of(
                        top_pixels[pixel] or canvas_colour,
                        bottom_pixels[pixel] or canvas_colour,
                    )
                    for pixel in range(width)
                ]
            )
            .crop(scroll_x, scroll_x + self.scrollable_content_region.width)
            .simplify()
        )


### canvas.py ends here
