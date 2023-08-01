# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div
from typedhtml.uikit.util import add_val


def leader(
    *args: Any, fill: Optional[str] = None, **kwargs: Unpack[GLOBAL_ATTR]
) -> div:
    """Create dot leaders for pricing menus or tables of contents.

    see: `https://getuikit.com/docs/leader`_
    """
    _fill = f"fill: {fill};" if fill else ""
    add_val("uk-leader", f"{_fill}", kwargs)  # type: ignore
    return div(*args, **kwargs)
