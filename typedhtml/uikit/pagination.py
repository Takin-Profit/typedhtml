# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import ul
from typedhtml.uikit.types import FlexClass
from typedhtml.uikit.util import add_val


def pagination(
    *args: Any, classes: Optional[list[FlexClass]], **kwargs: Unpack[GLOBAL_ATTR]
) -> ul:
    """Easily create a nice looking pagination to navigate through pages.

    see: `https://getuikit.com/docs/pagination`
    """
    _flex = " ".join(classes) if classes else ""
    add_val("cls", "uk-pagination {_flex}".strip(), kwargs)  # type: ignore
    return ul(*args, **kwargs)
