# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div
from typedhtml.uikit.types import Padding
from typedhtml.uikit.util import add_val


def tile(
    *args: Any,
    style_: Literal[
        "default",
        "muted",
        "primary",
        "secondary",
    ] = "default",
    padding: Optional[Padding] = None,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    _padding = f" uk-padding-{padding}" if padding else ""
    add_val("cls", f"uk-tile uk-tile-{style_}{_padding}", kwargs)  # type: ignore
    return div(*args, **kwargs)
