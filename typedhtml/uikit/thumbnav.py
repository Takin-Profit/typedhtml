# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from typing import Any, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import ul
from typedhtml.uikit.util import add_val


def thumbnav(
    *args: Any, is_vertical: bool = False, **kwargs: Unpack[GLOBAL_ATTR]
) -> ul:
    _vert = " uk-thumbnav-vertical" if is_vertical else ""
    add_val("cls", f"uk-thumbnav{_vert}", kwargs)  # type: ignore
    return ul(*args, **kwargs)
