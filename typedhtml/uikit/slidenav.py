# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import a, div
from typedhtml.uikit.types import Inverse, Position
from typedhtml.uikit.util import add_val


def slidenav_container(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> div:
    """To display a conjoint slidenav, wrap the slidenav items inside a <div> element
    and add the .uk-slidenav-container class, as well as one of the .uk-position-*
    classes.

    see: `https://getuikit.com/docs/slidenav`_
    """

    add_val("cls", "uk-slidenav-container", kwargs)  # type: ignore
    return div(*args, **kwargs)


def slidenav(
    *args: Any,
    direction: Literal["previous", "next"],
    position: Optional[Position] = None,
    inverse: Optional[Inverse] = None,
    large: bool = False,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> a:
    """Defines a navigation with previous and next buttons to flip through slideshows.

    see: `https://getuikit.com/docs/slidenav`_
    """
    _large = "uk-slidenav-large" if large else ""
    _pos = position or ""
    _inverse = inverse or ""
    add_val(f"uk-slidenav-{direction}", "", kwargs)  # type: ignore
    add_val("cls", f"{_large} {_pos} {_inverse}".strip(), kwargs)  # type: ignore
    return a(*args, **kwargs)
