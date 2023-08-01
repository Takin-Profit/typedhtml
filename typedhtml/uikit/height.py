# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div
from typedhtml.uikit.util import add_val

Height = Literal[
    "height_1_1",
    "height_small",
    "height_max_small",
    "height_medium",
    "height_max_medium",
    "height_large",
    "height_max_large",
]

Offset = Literal["top", "bottom", "expand"]


def height(
    *args: Any,
    val: Height,
    viewport: Optional[Offset] = None,
    min_height: Optional[int] = None,
    height_match: Optional[str] = None,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """UIkit's Height component offers three options to set heights: using simple fixed
    height utility classes, depending on the viewport or by matching the heights of
    different elements."""

    _offset = f"offset-{viewport}: true;" if viewport else ""
    _height = f"min-height: {str(min_height)};" if min_height else ""
    _match = height_match or ""
    if height_match:
        add_val("uk-height-match", _match, kwargs)  # type: ignore
    add_val("cls", val, kwargs)  # type: ignore
    add_val("uk-height-viewport", f"{_offset} {_height}".strip(), kwargs)  # type: ignore
    return div(*args, **kwargs)
