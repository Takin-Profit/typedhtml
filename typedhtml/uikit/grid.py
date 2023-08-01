# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div
from typedhtml.uikit.types import FlexClass, GridGap
from typedhtml.uikit.util import add_val


def grid(
    *args: Any,
    gaps: Optional[list[GridGap]] = None,
    flex: Optional[list[FlexClass]] = None,
    use_divider: bool = False,
    match_height: bool = False,
    masonry: bool = False,
    parallax: Optional[int] = None,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """The Grid system of UIkit allows you to arrange block elements in columns.
    It works closely together with the Width component to determine how much space of
    the container each item will take up, and it can also be combined with the
    Flex component to align and order grid items."""

    _gap = " ".join(gaps) if gaps else ""
    _flex = " ".join(flex) if flex else ""
    _div = " uk-grid-divider" if use_divider else ""
    _match = " uk-grid-match" if match_height else ""
    _masonry = " masonry: true;" if masonry else ""
    _parallax = f" parallax: {str(parallax)};" if parallax else ""
    add_val("cls", f"{_gap} {_div} {_match} {_flex}".strip(), kwargs)  # type: ignore
    add_val("uk-grid", f"{_masonry}{_parallax}", kwargs)  # type: ignore
    return div(*args, **kwargs)
