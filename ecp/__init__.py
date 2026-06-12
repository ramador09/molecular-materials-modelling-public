"""
Elementary Computational Physics — shared notebook support package.

Importing ``ecp`` gives notebooks a small, stable surface:

    from ecp import header, use_style, animate, validate, draw

Everything that defines the *look and feel* and the *correctness discipline*
of the series lives here, so the whole course can be restyled or re-checked by
editing one package rather than dozens of notebooks.
"""
from . import animate, draw, validate
from .style import AUTHOR, SERIES_TITLE, SERIES_VERSION, footer, header, use_style

__all__ = [
    "header",
    "footer",
    "use_style",
    "animate",
    "draw",
    "validate",
    "SERIES_TITLE",
    "SERIES_VERSION",
    "AUTHOR",
]

__version__ = SERIES_VERSION
