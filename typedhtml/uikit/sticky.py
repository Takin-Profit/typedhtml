# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Optional, Union, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div
from typedhtml.uikit.types import Animation
from typedhtml.uikit.util import add_val


def sticky(
    *args: Any,
    start: Optional[str] = None,
    end: Optional[str] = None,
    offset: Optional[int] = None,
    media: Optional[Union[str, int]] = None,
    animation: Optional[Animation] = None,
    show_on_up: bool = False,
    bottom: bool = False,
    overflow_flip: bool = False,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """Create a sticky element.

    see: `https://getuikit.com/docs/sticky`_
    """
    _ani = f" animation: {animation};" if animation else ""
    _offset = f" offset: {offset};" if offset else ""
    _end = f" end: {end};" if end else ""
    _start = f" start: {start};" if start else ""
    _pos = " position: bottom;" if bottom else ""
    _show_on_up = " show-on-up: true;" if show_on_up else ""
    _media = f" media: {media};" if media else ""
    o_flip = " overflow-flip: true;" if overflow_flip else ""
    add_val(
        "uk-sticky",
        (
            f"{_start}{_end}{_offset}{_pos}" + f"{_ani}{_show_on_up}{_media}{o_flip}"
        ).strip(),
        kwargs,  # type: ignore
    )
    return div(*args, **kwargs)
