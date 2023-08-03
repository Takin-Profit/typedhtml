# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div
from typedhtml.uikit.util import add_val

Pos = Literal[
    "top",
    "top-left",
    "top-right",
    "bottom",
    "bottom-left",
    "bottom-right",
    "left",
    "right",
]


def tooltip(
    *args: Any,
    text: str,
    pos: Optional[Pos],
    delay: Optional[int] = None,
    offset: Optional[int] = None,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """Easily create a nice looking tooltip.

    see: `https://getuikit.com/docs/tooltip`
    """
    _offset = f" offset: {offset};" if offset else ""
    _pos = f" pos: {pos};" if pos else ""
    _delay = f" delay: {delay};" if delay else ""
    add_val("uk-tooltip", f"title: {text};{_pos}{_delay}{_offset}", kwargs)  # type: ignore
    return div(*args, **kwargs)
