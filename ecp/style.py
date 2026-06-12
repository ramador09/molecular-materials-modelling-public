"""
ecp.style
=========

Single source of truth for the *visual identity* of the
**Elementary Computational Physics** notebook series.

Every notebook's first code cell calls :func:`header`, so the look of the
entire course is defined here and nowhere else. Change the design in this
file and *all* notebooks update on the next build. That is the whole point:
the course is a living document, and its appearance is centralised.

The header is emitted as self-contained HTML with inline styles so it renders
correctly in a bare notebook viewer (nbviewer, JupyterLab, VS Code). The
book-level chrome (site nav, fonts, code blocks) is themed separately in
``_static/ecp.css``.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from html import escape

import matplotlib.pyplot as plt

# --------------------------------------------------------------------------- #
#  Design tokens — the ONE place to edit colours, fonts, and series metadata. #
# --------------------------------------------------------------------------- #

SERIES_TITLE = "Molecular and Materials Modelling"
SERIES_SUBTITLE = "A Computational Materials Science Notebook Companion"
AUTHOR = "Raymond Amador"

# Bumped by tools/bump_version.py / edited by hand; shown in every header.
SERIES_VERSION = "0.1.0"

# Refined editorial / scientific-manuscript palette.
# Deep ink + warm amber accent on a faint parchment panel. Deliberately not
# the generic blue-on-white or purple-gradient AI look.
INK = "#16213e"          # near-navy, primary text
INK_SOFT = "#46506b"     # secondary text / metadata
ACCENT = "#c0851a"       # warm amber rule + numerals
PANEL = "#faf7f0"        # parchment header background
HAIRLINE = "#dcd6c8"     # subtle dividers

DISPLAY_FONT = "'Fraunces', 'Iowan Old Style', Georgia, serif"
BODY_FONT = "'Source Serif 4', 'Iowan Old Style', Georgia, serif"
MONO_FONT = "'JetBrains Mono', 'SFMono-Regular', Menlo, Consolas, monospace"

# Google Fonts import. Harmless if offline (falls back to the serifs above).
_FONT_IMPORT = (
    "@import url('https://fonts.googleapis.com/css2?"
    "family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,900&"
    "family=Source+Serif+4:wght@400;600&"
    "family=JetBrains+Mono:wght@400;600&display=swap');"
)


@dataclass
class Notebook:
    """Lightweight metadata describing one notebook in the series."""

    volume: str          # e.g. "Volume I — Elementary Mechanics"
    number: str          # e.g. "1.3"
    title: str           # e.g. "The Double Pendulum"
    blurb: str = ""       # one-line description shown under the title
    difficulty: str = ""  # "introductory" | "intermediate" | "advanced"
    estimate: str = ""    # rough time, e.g. "60–90 min"
    source: str = ""      # source lecture, e.g. "FS 2023 · Lecture 2 (Monte Carlo)"


def header(
    volume: str,
    number: str,
    title: str,
    blurb: str = "",
    difficulty: str = "",
    estimate: str = "",
    source: str = "",
):
    """Return the series header for a notebook as a rich HTML display object.

    Usage (first code cell of every notebook)::

        from ecp.style import header
        header(
            volume="Volume I — Elementary Mechanics",
            number="1.3",
            title="The Double Pendulum",
            blurb="Chaos, energy conservation, and animation from a Lagrangian.",
            difficulty="intermediate",
            estimate="60–90 min",
        )
    """
    nb = Notebook(volume, number, title, blurb, difficulty, estimate, source)
    return _Html(_render(nb))


def _meta_line(nb: "Notebook") -> str:
    parts = []
    if nb.difficulty:
        parts.append(f"Level&nbsp;&middot;&nbsp;{escape(nb.difficulty)}")
    if nb.estimate:
        parts.append(f"Est.&nbsp;&middot;&nbsp;{escape(nb.estimate)}")
    if not parts:
        return ""
    sep = "&nbsp;&nbsp;&nbsp;&#8226;&nbsp;&nbsp;&nbsp;"  # spaced bullet, renderer-proof
    inner = sep.join(parts)
    return (
        f"<div class='ecp-meta' style='font-family:{MONO_FONT};font-size:11px;"
        f"letter-spacing:.08em;text-transform:uppercase;color:{INK_SOFT};'>"
        f"{inner}</div>"
    )


def _render(nb: Notebook) -> str:
    today = date.today().isoformat()
    chips = _meta_line(nb)
    return f"""
<style>{_FONT_IMPORT}</style>
<div style="
    font-family:{BODY_FONT};
    background:{PANEL};
    border:1px solid {HAIRLINE};
    border-left:6px solid {ACCENT};
    border-radius:6px;
    padding:26px 30px 22px 30px;
    margin:4px 0 26px 0;
    box-shadow:0 1px 0 rgba(0,0,0,.03), 0 8px 24px -18px rgba(22,33,62,.5);">

  <div style="font-family:{MONO_FONT};font-size:12px;letter-spacing:.12em;
              text-transform:uppercase;color:{ACCENT};font-weight:600;
              margin-bottom:4px;">
    {escape(SERIES_TITLE)}
  </div>

  <div style="display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;">
    <span style="font-family:{DISPLAY_FONT};font-weight:900;font-size:22px;
                 line-height:1.1;color:{INK};
                 font-variation-settings:'opsz' 144;">
      {escape(nb.volume)}
    </span>
    <span style="font-family:{MONO_FONT};font-size:12px;letter-spacing:.06em;
                 color:{INK_SOFT};">
      Notebook&nbsp;{escape(nb.number)}
    </span>
  </div>

  {f'''<div style="font-family:{BODY_FONT};font-size:15px;color:{INK_SOFT};
                   margin-top:10px;max-width:62ch;">{escape(nb.blurb)}</div>'''
    if nb.blurb else ''}

  {f'''<div style="font-family:{MONO_FONT};font-size:11px;letter-spacing:.04em;
                   color:{ACCENT};margin-top:10px;">Based on {escape(nb.source)}</div>'''
    if nb.source else ''}

  <div style="margin-top:16px;">{chips}</div>

  <div style="border-top:1px solid {HAIRLINE};margin-top:16px;padding-top:12px;
              display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;
              font-family:{MONO_FONT};font-size:11px;color:{INK_SOFT};
              letter-spacing:.04em;">
    <span>{escape(AUTHOR)}</span>
    <span>v{escape(SERIES_VERSION)} &nbsp;·&nbsp; {today} &nbsp;·&nbsp;
          CC&nbsp;BY&nbsp;4.0 (text) / MIT (code)</span>
  </div>
</div>
""".strip()


def use_style() -> None:
    """Apply the series Matplotlib style.

    Notebooks call this once after the header. The style lives in
    ``ecp/ecp.mplstyle`` and is shipped as package data, so it is found in
    every install mode: an editable dev checkout, a built wheel, and Colab's
    ``pip install git+...`` (where ``ecp`` lives in site-packages). Figure
    aesthetics are thus centralised here, like the header.
    """
    from importlib.resources import as_file, files
    from pathlib import Path

    # Primary: the copy packaged inside ``ecp`` (works in all install modes).
    try:
        resource = files("ecp").joinpath("ecp.mplstyle")
        with as_file(resource) as path:
            if path.exists():
                plt.style.use(str(path))
                return
    except (FileNotFoundError, ModuleNotFoundError, OSError):
        pass

    # Legacy fallback: a copy at the repository root (older checkouts).
    legacy = Path(__file__).resolve().parent.parent / "ecp.mplstyle"
    if legacy.exists():
        plt.style.use(str(legacy))


class _Html:
    """Minimal rich-display wrapper so the header shows without importing
    IPython at module level (keeps ``ecp`` importable in plain scripts/CI)."""

    def __init__(self, html: str):
        self._html = html

    def _repr_html_(self) -> str:  # noqa: D401  (IPython display protocol)
        return self._html

    def __repr__(self) -> str:
        return f"<ECP header: {len(self._html)} chars of HTML>"


# --------------------------------------------------------------------------- #
#  Footer: download invitation + "contact for solutions" note.                #
#  Centralised so one edit changes the note across every notebook.            #
# --------------------------------------------------------------------------- #

CONTACT = "hello@ramador.me"  # email -> mailto:, anything with "://" -> link

# Course-wide provenance. Rendered in every footer so the attribution to the
# original ETH course appears on every page from one edit (the living-document
# principle). Per-notebook nuance still goes in that notebook's overview.
PROVENANCE = (
    "Based on the lecture and exercise materials of <b>Molecular and Materials "
    "Modelling</b> (ETH Z&uuml;rich and Empa, FS&nbsp;2023), developed by "
    "Prof.&nbsp;Dr.&nbsp;Daniele Passerone (lectures), Dr.&nbsp;Carlo Pignedoli, "
    "and the author (exercises); here synthesised, expanded, and restyled by the "
    "author."
)


def footer(contact: str | None = None):
    """Return the series footer: a branded callout inviting download and
    pointing readers to you for the reference solutions.

    Place as the LAST cell of every notebook::

        from ecp.style import footer
        footer()

    The notebook offered by the toolbar download button is the public,
    solution-free build, so this note is consistent with what readers receive.
    """
    contact = contact or CONTACT
    if "@" in contact and "://" not in contact:
        href = f"mailto:{escape(contact)}"
    else:
        href = escape(contact)
    link = (
        f"<a href='{href}' style='color:{ACCENT};text-decoration:none;"
        f"border-bottom:1px solid {ACCENT};'>{escape(contact)}</a>"
    )

    html = f"""
<style>{_FONT_IMPORT}</style>
<div style="font-family:{BODY_FONT};background:{PANEL};border:1px solid {HAIRLINE};
            border-left:6px solid {ACCENT};border-radius:6px;
            padding:18px 22px;margin:30px 0 8px 0;">
  <div style="font-family:{MONO_FONT};font-size:11px;letter-spacing:.12em;
              text-transform:uppercase;color:{ACCENT};font-weight:600;
              margin-bottom:6px;">Take this notebook with you</div>
  <div style="font-size:14.5px;color:{INK};line-height:1.55;max-width:66ch;">
    Use the download button (&#8595;) in the toolbar above to save this notebook
    and run it yourself. The published notebooks ship <b>without worked
    solutions</b>; if you would like the reference solutions &mdash; to teach
    from or to check your own work &mdash; get in touch: {link}.
  </div>
  <div style="font-size:12px;color:{INK_SOFT};line-height:1.5;max-width:66ch;
              margin-top:10px;border-top:1px solid {HAIRLINE};padding-top:8px;">
    {PROVENANCE}
  </div>
</div>
""".strip()
    return _Html(html)
