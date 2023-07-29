# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Optional, Unpack, cast

from typedhtml.attributes import li_attr
from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import a, div, li, ul
from typedhtml.uikit.base import Transition
from typedhtml.uikit.util import add_val


def accordion(
    collapsible: bool = True,
    multiple: bool = False,
    transition: Optional[Transition] = None,
    *args: Any,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> ul:
    """Create a list of items that can be shown individually by clicking an item's
    header.

    see: `https://getuikit.com/docs/accordion`_
    """
    opts: list[str] = []
    if not collapsible:
        opts.append("collapsible: false;")
    if multiple:
        opts.append("multiple: true;")
    if transition is not None:
        opts.append(f"transition: {transition};")

    cast(dict[str, str], kwargs)["uk-accordion"] = " ".join(opts)

    return ul(*args, **kwargs)


def accordion_item(
    is_open: bool = False,
    *args: Any,
    **kwargs: Unpack[li_attr],
) -> li:
    """Create an item for an accordion.

    see: `https://getuikit.com/docs/accordion`_
    """
    if is_open:
        add_val("cls", "uk-open", kwargs)  # type: ignore

    return li(*args, **kwargs)


def accordion_title(
    title: str = "", href: str = "#", *args: Any, **kwargs: Unpack[li_attr]
) -> a:
    """Create a title for an accordion item.

    see: `https://getuikit.com/docs/accordion`_
    """
    add_val("cls", "uk-accordion-title", kwargs)  # type: ignore
    add_val("href", href, kwargs)  # type: ignore
    return a(title, *args, **kwargs)


def accordion_content(
    *args: Any,
    **kwargs: Unpack[li_attr],
) -> div:
    """Create content for an accordion item.

    see: `https://getuikit.com/docs/accordion`_
    """
    add_val("cls", "uk-accordion-content", kwargs)  # type: ignore
    return div(*args, **kwargs)
