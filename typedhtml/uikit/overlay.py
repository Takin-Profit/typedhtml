# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div, span
from typedhtml.uikit.types import Position
from typedhtml.uikit.util import add_val

Style = Literal["default", "primary"]


def overlay(
    *args: Any,
    style_: Style = "default",
    pos: Optional[Position] = None,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """Create an image overlay, which comes in different styles.

    see: `https://getuikit.com/docs/overlay`"""

    add_val("cls", f"uk-overlay {pos} {style_}", kwargs)  # type: ignore
    return div(*args, **kwargs)


def overlay_icon(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> span:
    """Create an image overlay, which comes in different styles.

    see: `https://getuikit.com/docs/overlay`"""

    add_val("cls", "uk-overlay-icon", kwargs)  # type: ignore
    return span(*args, **kwargs)
