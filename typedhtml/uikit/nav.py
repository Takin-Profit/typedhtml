# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Unpack

from typedhtml.attributes import li_attr
from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import li, ul
from typedhtml.uikit.util import add_val

Style = Literal["default", "primary", "secondary"]


def nav(
    *args: Any,
    style_: Style = "default",
    center: bool = False,
    divider: bool = False,
    dropdown: bool = False,
    navbar: bool = False,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> ul:
    """Defines different styles for list navigations.

    see: `https://getuikit.com/docs/nav`
    """

    _center = " uk-nav-center" if center else ""
    _divider = " uk-nav-divider" if divider else ""
    _drop = " uk-dropdown-nav" if dropdown else ""
    _navbar = " uk-navbar-dropdown-nav" if navbar else ""
    add_val(
        "cls",
        f"uk-nav uk-nav-{style_}{_center}{_divider}" + f"{_drop}{_navbar}",
        kwargs,  # type: ignore
    )
    return ul(*args, **kwargs)


def nav_item(
    *args: Any,
    is_active: bool = False,
    is_header: bool = False,
    use_divider: bool = False,
    **kwargs: Unpack[li_attr],
) -> li:
    """Defines different styles for list navigations.

    see: `https://getuikit.com/docs/nav`
    """
    _div = " uk-nav-divider" if use_divider else ""
    _header = " uk-nav-header" if is_header else ""
    _active = " uk-active" if is_active else ""
    add_val("cls", f"_{_active}{_header}{_div}", kwargs)  # type: ignore
    return li(*args, **kwargs)
