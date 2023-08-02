# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import ul
from typedhtml.uikit.util import add_val


def tab(
    *args: Any,
    bottom: bool = False,
    direction: Optional[Literal["left", "right"]],
    media: Optional[str] = None,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> ul:
    """Create a tabbed navigation with different styles..

    see: `https://getuikit.com/docs/tab`_
    """

    _media = f" media: {media};" if media else ""
    _bottom = " uk-tab-bottom" if bottom else ""
    _dir = f" uk-tab-{direction}" if direction else ""
    add_val("uk-tab", f"{_media}", kwargs)  # type: ignore
    add_val("cls", f"{_bottom}{_dir}", kwargs)  # type: ignore
    return ul(*args, **kwargs)
