# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Unpack

from typedhtml.attributes import a_attr, li_attr
from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import a, div, li, ul
from typedhtml.tags import nav as navi
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


def navbar(
    *args: Any,
    container: bool = False,
    transparent: bool = False,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> navi:
    """Create a navigation bar with dropdown menus for the main site navigation.

    see: `https://getuikit.com/docs/navbar`
    """
    add_val("uk-navbar", "", kwargs)  # type: ignore
    _transparent = " uk-navbar-transparent" if transparent else ""
    _container = " uk-navbar-container" if container else ""
    add_val("cls", f"{_container}{_transparent}", kwargs)  # type: ignore
    return navi(*args, **kwargs)


def navbar_align(
    *args: Any,
    direction: Literal[
        "left",
        "right",
        "center",
    ],
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """Align the navbar content to the left, right or center.

    see: `https://getuikit.com/docs/navbar`
    """
    _dir = f"uk-navbar-{direction}"

    add_val("cls", _dir, kwargs)  # type: ignore
    return div(*args, **kwargs)


def navigation(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> ul:
    """<ul> element that creates the navigation.

    see:  `https://getuikit.com/docs/navbar`
    """

    add_val("cls", "uk-navbar-nav", kwargs)  # type: ignore
    return ul(*args, **kwargs)


def navbar_item(
    *args: Any,
    source: str,
    anchor: str,
    is_parent: bool = False,
    is_active: bool = False,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> li:
    """<li> element that creates the navigation items.
        contains an <a> element that defines the link.
        source param defines the anchor href.

    see:  `https://getuikit.com/docs/navbar`
    """
    _parent = " uk-parent" if is_parent else ""
    _active = " uk-active" if is_active else ""
    add_val("cls", f"{_parent}{_active}", kwargs)  # type: ignore
    list_item = li(*args, **kwargs)
    with list_item:
        a(anchor, href=source)
    return list_item


def navbar_subtitle(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> div:
    """<div> element that creates the navbar subtitle.

    see:  `https://getuikit.com/docs/navbar`
    """
    add_val("cls", "uk-navbar-subtitle", kwargs)  # type: ignore
    return div(*args, **kwargs)


def navbar_toggle(*args: Any, animate: bool = False, **kwargs: Unpack[a_attr]) -> a:
    """<a> element that creates the navbar toggle.

    see:  `https://getuikit.com/docs/navbar`
    """
    _animate = " uk-navbar-toggle-animate" if animate else ""
    add_val("cls", f"uk-navbar-toggle{_animate}", kwargs)  # type: ignore
    add_val("href", "#", kwargs)  # type: ignore
    add_val("uk-navbar-toggle-icon", "", kwargs)  # type: ignore
    return a(*args, **kwargs)
