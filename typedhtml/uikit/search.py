# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Unpack

from typedhtml.attributes import form_attr
from typedhtml.tags import a, form, input_
from typedhtml.uikit.util import add_val


def search(
    *args: Any,
    search_icon: bool = True,
    navbar: bool = False,
    toggle: bool = False,
    navbar_toggle: bool = False,
    size_: Literal["default", "large"] = "default",
    **kwargs: Unpack[form_attr],
) -> form:
    """Easily create a nice looking search.

    see: `https://getuikit.com/docs/search`
    """
    _size = f" uk-search-{size_}"
    _nav = " uk-search-navbar" if navbar else ""
    _toggle = " uk-search-toggle" if toggle else ""
    _nav_toggle = " uk-navbar-toggle" if navbar_toggle else ""
    add_val("cls", f"uk-search{_size}{_nav}", kwargs)  # type: ignore
    add_val("aria-label", "Search", kwargs)  # type: ignore
    _form = form(*args, **kwargs)
    with _form:
        a(cls=f"{_toggle}{_nav_toggle}".strip(), uk_search_icon="" if search_icon else None)  # type: ignore
        input_(
            cls="uk-search-input",
            type_="search",
            placeholder="Search...",
            aria_label="Search",  # type: ignore
        )

    return _form
