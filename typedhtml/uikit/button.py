# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from typing import Any, Literal, Optional, Unpack

from typedhtml.attributes import button_attr
from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import button as btn
from typedhtml.tags import div
from typedhtml.uikit.types import Width

from .util import add_val

Style = Literal["default", "primary", "secondary", "danger", "text", "link"]


def _size(size: Literal["default", "small", "large"]):
    return "" if size == "default" else f"uk-button-{size}"


def _width(width: Optional[Width]):
    return "" if width is None else width


def button(
    *args: Any,
    style_: Style = "default",
    size: Literal["default", "small", "large"] = "default",
    width: Optional[Width] = None,
    **kwargs: Unpack[button_attr],
) -> btn:
    """Button is a control that is used to trigger an action.

    see: `https://getuikit.com/docs/button`
    """
    add_val("cls", f"uk-button uk-button-{style_} {_size(size)} {_width(width)}".strip(" "), kwargs)  # type: ignore
    return btn(*args, **kwargs)


def close_button(*args: Any, **kwargs: Unpack[button_attr]) -> btn:
    """Create a close icon that can be combined with different components.
    see: `https://getuikit.com/docs/close`
    """
    add_val("cls", "uk-close", kwargs)  # type: ignore
    add_val("type_", "button", kwargs)  # type: ignore
    return btn(*args, **kwargs)


def button_group(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> div:
    """Button groups are useful when you want to group related buttons together.

    see: `https://getuikit.com/docs/button`
    """
    add_val("cls", "uk-button-group", kwargs)  # type: ignore
    return div(*args, **kwargs)
