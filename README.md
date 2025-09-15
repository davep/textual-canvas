# textual-canvas

![Being used for textual-mandelbrot](https://raw.githubusercontent.com/davep/textual-canvas/main/img/textual-mandelbrot.png)
*An example of `textual-canvas` being used in a Textual application*

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/davep/textual-canvas/code-checks.yaml)](https://github.com/davep/textual-canvas/actions)
[![GitHub commits since latest release](https://img.shields.io/github/commits-since/davep/textual-canvas/latest)](https://github.com/davep/textual-canvas/commits/main/)
[![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/davep/textual-canvas)](https://github.com/davep/textual-canvas/issues)
[![GitHub Release Date](https://img.shields.io/github/release-date/davep/textual-canvas)](https://github.com/davep/textual-canvas/releases)
[![PyPI - License](https://img.shields.io/pypi/l/textual-canvas)](https://github.com/davep/textual-canvas/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/textual-canvas)](https://github.com/davep/textual-canvas/blob/main/pyproject.toml)
[![PyPI - Version](https://img.shields.io/pypi/v/textual-canvas)](https://pypi.org/project/textual-canvas/)

## Introduction

`textual-canvas` provides a simple terminal-based drawing canvas widget for
use with [Textual](https://textual.textualize.io/). Initially developed as a
widget for building
[`textual-mandelbrot`](https://github.com/davep/textual-mandelbrot), it made
sense to spin it out into its own general-purpose library.

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

See [the documentation](https://textual-canvas.davep.dev/) for an
introduction, a usage guide and detailed API documentation.

[//]: # (README.md ends here)
