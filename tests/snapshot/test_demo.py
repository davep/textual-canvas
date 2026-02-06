"""Snapshot test the main 'demo' app."""

##############################################################################
# Python imports.
from collections.abc import Callable

##############################################################################
# Local imports.
from textual_canvas.__main__ import CanvasTestApp

##############################################################################
# Useful constants.
TERM = {"terminal_size": (122, 62)}


##############################################################################
def test_initial_screen(snap_compare: Callable[..., bool]) -> None:
    """Snapshot test for the main 'demo' screen."""

    assert snap_compare(CanvasTestApp(), **TERM)


##############################################################################
def test_red_canvas(snap_compare: Callable[..., bool]) -> None:
    """Snapshot test for the main 'demo' screen; canvas changed to red."""

    assert snap_compare(CanvasTestApp(), press=["r"], **TERM)


##############################################################################
def test_green_canvas(snap_compare: Callable[..., bool]) -> None:
    """Snapshot test for the main 'demo' screen; canvas changed to green."""

    assert snap_compare(CanvasTestApp(), press=["g"], **TERM)


##############################################################################
def test_blue_canvas(snap_compare: Callable[..., bool]) -> None:
    """Snapshot test for the main 'demo' screen; canvas changed to blue."""

    assert snap_compare(CanvasTestApp(), press=["b"], **TERM)


### test_demo.py ends here
