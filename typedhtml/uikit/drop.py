# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Any, Literal, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div
from typedhtml.uikit.util import add_val

DropMode = Literal["click,hover", "hover", "click"]

DropPos = Literal[
    "top-left",
    "top-center",
    "top-right",
    "bottom-left",
    "bottom-center",
    "bottom-right",
    "left-top",
    "left-center",
    "left-bottom",
    "right-top",
    "right-center",
    "right-bottom",
]

DropAnimation = Literal[
    "slide-top",
    "slide-bottom",
    "slide-left",
    "slide-right",
    "reveal-top",
    "reveal-bottom",
    "reveal-left",
    "reveal-right",
]


def _drop(
    is_dropdown: bool = False,
    mode: DropMode = "hover",
    pos: DropPos = "bottom-center",
    boundary: Optional[str] = None,
    target: Optional[str] = None,
    shift: bool = True,
    flip: bool = True,
    inset: bool = False,
    stretch: bool = False,
    auto_update: bool = True,
    animation: Optional[DropAnimation] = None,
    duration: Optional[int] = None,
    offset: Optional[int] = None,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> None:
    """Position any element in relation to another element.

    The Drop component is aim-aware. This means the drop stays open as long as the mouse
    pointer moves towards the drop. An additional delay ensures that the drop stays open
    even if the mouse pointer shortly moves in another direction. A drop closes
    immediately if another menu item is hovered.

        see: `https://getuikit.com/docs/drop`_
    """
    _down = "down" if is_dropdown else ""
    _shift = "" if shift else " shift: false;"
    _flip = "" if flip else " flip: false;"
    _auto_update = "" if auto_update else " auto-update: false;"
    _target = f" target: {target};" if target else ""
    _inset = " inset: true;" if inset else ""
    _stretch = " stretch: true;" if stretch else ""
    _animation = f" animation: {animation};" if animation else ""
    _duration = f" duration: {duration};" if duration else ""
    _offset = f" offset: {offset};" if offset else ""
    _boundary = f"boundary: {boundary};" if boundary else ""
    add_val(
        f"uk-drop{_down}",
        f"mode: {mode}; pos: {pos};"
        + f"{_boundary}{_shift}{_flip}"
        + f"{_auto_update}{_target}{_inset}{_stretch}"
        + f"{_animation}{_duration}{_offset}",
        kwargs,  # type: ignore
    )


def drop(
    *args: Any,
    mode: DropMode = "hover",
    pos: DropPos = "bottom-center",
    boundary: Optional[str] = None,
    target: Optional[str] = None,
    shift: bool = True,
    flip: bool = True,
    inset: bool = False,
    stretch: bool = False,
    auto_update: bool = True,
    animation: Optional[DropAnimation] = None,
    duration: Optional[int] = None,
    offset: Optional[int] = None,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """Position any element in relation to another element.

    The Drop component is aim-aware. This means the drop stays open as long as the mouse
    pointer moves towards the drop. An additional delay ensures that the drop stays open
    even if the mouse pointer shortly moves in another direction. A drop closes
    immediately if another menu item is hovered.

        see: `https://getuikit.com/docs/drop`_
    """
    _drop(
        mode=mode,
        pos=pos,
        boundary=boundary,
        target=target,
        shift=shift,
        flip=flip,
        inset=inset,
        stretch=stretch,
        auto_update=auto_update,
        animation=animation,
        duration=duration,
        offset=offset,
        **kwargs,
    )
    return div(*args, **kwargs)


DropBarDir = Literal["top", "bottom", "left", "right"]


def drop_bar(
    *args: Any,
    is_large: bool = False,
    direction: DropBarDir = "bottom",
    mode: DropMode = "hover",
    pos: DropPos = "bottom-center",
    boundary: Optional[str] = None,
    target: Optional[str] = None,
    shift: bool = True,
    flip: bool = True,
    inset: bool = False,
    stretch: bool = False,
    auto_update: bool = True,
    animation: Optional[DropAnimation] = None,
    duration: Optional[int] = None,
    offset: Optional[int] = None,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """Create a toggleable, full-width section called dropbar.

    The Dropbar component provides a section-like style for the Drop component.
    In opposite to the dropdown which is positioned anywhere on a page with space around
    , the dropbar extends to the full width or height of the viewport,
    so it perfectly fits three edges without spacing.

    The Dropbar component is aim-aware. This means the dropbar stays open as long as the
    mouse pointer moves towards the dropbar. An additional delay ensures that the
    dropbar stays open even if the mouse pointer shortly moves in another direction.
    A dropbar closes immediately if another dropbar is opened."""

    _dir = f"uk-dropbar-{direction};"
    _large = " uk-dropbar-large;" if is_large else ""
    add_val("cls", f"uk-dropbar {_dir}{_large}", kwargs)  # type: ignore
    _drop(
        mode=mode,
        pos=pos,
        boundary=boundary,
        target=target,
        shift=shift,
        flip=flip,
        inset=inset,
        stretch=stretch,
        auto_update=auto_update,
        animation=animation,
        duration=duration,
        offset=offset,
        **kwargs,
    )

    return div(*args, **kwargs)


def dropdown(
    *args: Any,
    mode: DropMode = "hover",
    pos: DropPos = "bottom-center",
    boundary: Optional[str] = None,
    target: Optional[str] = None,
    shift: bool = True,
    flip: bool = True,
    inset: bool = False,
    stretch: bool = False,
    auto_update: bool = True,
    animation: Optional[DropAnimation] = None,
    duration: Optional[int] = None,
    offset: Optional[int] = None,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """Defines different styles for a toggleable dropdown.

    The Dropdown component is aim-aware. This means the dropdown stays open as long as
    the mouse pointer moves towards the dropdown. An additional delay ensures that the
    dropdown stays open even if the mouse pointer shortly moves in another direction.
    A dropdown closes immediately if another menu item is hovered."""
    _drop(
        is_dropdown=True,
        mode=mode,
        pos=pos,
        boundary=boundary,
        target=target,
        shift=shift,
        flip=flip,
        inset=inset,
        stretch=stretch,
        auto_update=auto_update,
        animation=animation,
        duration=duration,
        offset=offset,
        **kwargs,
    )

    return div(*args, **kwargs)
