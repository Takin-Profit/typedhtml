# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import ul
from typedhtml.uikit.util import add_val


def subnav(
    *args: Any, divider: bool = False, pill: bool = False, **kwargs: Unpack[GLOBAL_ATTR]
) -> ul:
    """Defines different styles for a sub navigation.

    see: `https://getuikit.com/docs/subnav`_
    """

    _pill = " uk-subnav-pill" if pill else ""
    _divider = " uk-subnav-divider" if divider else ""
    add_val("cls", f"uk-subnav{_divider}{_pill}", kwargs)  # type: ignore
    return ul(*args, **kwargs)
