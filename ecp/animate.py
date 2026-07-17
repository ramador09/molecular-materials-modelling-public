"""
ecp.animate
===========

Centralised animation strategy.

GitHub Pages serves a *static* site with no running Python kernel, so live
``FuncAnimation`` objects cannot recompute in the browser. The course policy
is therefore: pre-render every animation to a self-contained HTML5/JS player
with :func:`matplotlib.animation.Animation.to_jshtml`. The embedded player
ships inside the page and plays for any visitor, no server required.

Notebooks should always wrap their animations with :func:`show` rather than
calling ``to_jshtml`` directly, so playback behaviour *and frame size* are
defined in one place.

Why frame size matters: ``to_jshtml`` embeds every frame as a base64 PNG, and
matplotlib silently **drops frames** once the embed exceeds
``animation.embed_limit`` (20 MB by default). Worse, the frames are rendered
through ``savefig``, so they inherit ``savefig.dpi`` — which the series style
sets to 150 for crisp static figures. At 150 dpi a modest animation blows past
20 MB and the player breaks. :func:`show` therefore renders frames in a
temporary rc context with a sensible *frame* dpi and a raised embed limit, so
animations stay lean and complete without the author having to think about it.
"""
from __future__ import annotations

import matplotlib as mpl
from matplotlib.animation import Animation

# Series-wide playback defaults.
DEFAULT_FPS = 30
DEFAULT_MODE = "loop"        # "loop" | "once" | "reflect"

# Frame-rendering defaults (the fix). Keep animations small enough to embed
# fully in a static page. 90 dpi is plenty for on-screen playback; raise only
# if a specific animation needs more detail.
FRAME_DPI = 90
EMBED_LIMIT_MB = 60          # generous safety net so frames are never dropped


def show(
    anim: Animation,
    *,
    fps: int = DEFAULT_FPS,
    mode: str = DEFAULT_MODE,
    frame_dpi: int = FRAME_DPI,
    embed_limit_mb: float = EMBED_LIMIT_MB,
):
    """Return a notebook-displayable, kernel-free HTML player for an animation.

    Every frame is baked to a base64 PNG and embedded in a self-contained HTML
    player (``Animation.to_jshtml``), so the animation replays on the static site
    with no live kernel, the course policy for shipping motion to a non-running
    reader. Frames render at ``frame_dpi`` (independent of the figure's
    ``savefig.dpi``) and the embed limit is raised so nothing is silently truncated.

    Parameters
    ----------
    anim : matplotlib.animation.Animation
        The animation to embed, typically a ``FuncAnimation``.
    fps : int, optional
        Playback frames per second (default :data:`DEFAULT_FPS`).
    mode : str, optional
        Player loop mode, e.g. ``"loop"`` or ``"once"`` (default :data:`DEFAULT_MODE`).
    frame_dpi : int, optional
        Resolution at which frames are rasterised (default :data:`FRAME_DPI`).
    embed_limit_mb : float, optional
        Maximum embedded size in MB before matplotlib truncates (default
        :data:`EMBED_LIMIT_MB`).

    Returns
    -------
    IPython.display.HTML
        The embedded player; return it as a cell's last expression to display it.

    Notes
    -----
    Aim for a few hundred frames (≲ 300). If a player feels heavy, reduce the frame
    count at construction rather than the dpi here. Call ``plt.close(fig)`` before
    ``show`` so the static figure is not also rendered.

    Example
    -------
    ::

        anim = FuncAnimation(fig, update, frames=N, blit=True)
        plt.close(fig)            # don't also show the static figure
        from ecp.animate import show
        show(anim)                # last line of the cell -> renders the player
    """
    from IPython.display import HTML

    with mpl.rc_context(
        {"savefig.dpi": frame_dpi, "animation.embed_limit": embed_limit_mb}
    ):
        html = anim.to_jshtml(fps=fps, default_mode=mode)
    return HTML(html)
