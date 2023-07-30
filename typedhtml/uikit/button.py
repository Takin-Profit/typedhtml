# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from typing import Any, Literal, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import button as btn
from typedhtml.tags import div
from typedhtml.uikit.types import Width

from .util import add_val

Style = Literal["default", "primary", "secondary", "danger", "text", "link"]


def size(size: Literal["default", "small", "large"]):
    return "" if size == "default" else f"uk-button-{size}"


def width(width: Optional[Width]):
    return "" if width is None else width


def button(
    *args,
    style: Style = "default",
    size: Literal["default", "small", "large"],
    width: Optional[Width] = None,
    **kwargs,
):
    """Button is a control that is used to trigger an action.

    see: `https://getuikit.com/docs/button`
    """
    add_val("cls", f"uk-button uk-button-{style} {size(size)} {width(width)}", kwargs)  # type: ignore
    return btn(*args, **kwargs)


def button_group(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> div:
    """Button groups are useful when you want to group related buttons together.

    see: `https://getuikit.com/docs/button`
    """
    add_val("cls", "uk-button-group", kwargs)  # type: ignore
    return div(*args, **kwargs)
