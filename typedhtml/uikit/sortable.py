# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div
from typedhtml.uikit.util import add_val


def sortable(
    *args: Any,
    handle: Optional[str] = None,
    group: Optional[str] = None,
    custom: Optional[str] = None,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """Create sortable grids and lists to rearrange the order of its elements.

    see: `https://getuikit.com/docs/sortable`_
    """
    _handle = f"handle: {handle};" if handle else ""
    _group = f" group: {group};" if group else ""
    _custom = f" cls-custom:{custom};" if custom else ""
    add_val("uk-sortable", f"{_handle}{_group}{_custom}", kwargs)  # type: ignore
    return div(*args, **kwargs)
