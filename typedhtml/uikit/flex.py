# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div
from typedhtml.uikit.types import FlexClass
from typedhtml.uikit.util import add_val


def flex(
    *args: Any,
    classes: Optional[list[FlexClass]] = None,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """Create dropdown menus for any navigation.

    The Dropnav component initializes all dropdowns in a navigation with the same
    options,
    so they don't have to be initialized individually. All dropdowns within the dropnav
    are aim-aware. This means the dropdowns stay open as long as the mouse pointer moves
    towards the dropdown. An additional delay ensures that dropdowns stay open even if
    the
    mouse pointer shortly moves in another direction. In hover mode dropdowns close
    immediately if another menu item is hovered."""

    _align = " ".join(classes) if classes else ""
    add_val("cls", f"uk-flex {_align}", kwargs)  # type: ignore
    return div(*args, **kwargs)
