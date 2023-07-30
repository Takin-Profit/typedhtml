# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import ul
from typedhtml.uikit.util import add_val


def breadcrumb(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> ul:
    """Breadcrumb is a secondary navigation scheme that indicates the user's location
    in a website or application.

    see: `https://getuikit.com/docs/breadcrumb`
    """
    add_val("cls", "uk-breadcrumb", kwargs)  # type: ignore
    return ul(*args, **kwargs)
