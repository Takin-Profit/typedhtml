# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div
from typedhtml.uikit.util import add_val


def description_list(
    *args: Any, use_divider: bool, **kwargs: Unpack[GLOBAL_ATTR]
) -> div:
    """Easily create nice looking description lists, which come in different styles.

    see: `https://getuikit.com/docs/description-list`_
    """

    add_val("cls", "uk-description-list", kwargs)  # type: ignore
    if use_divider:
        add_val("cls", "uk-description-list-divider", kwargs)  # type: ignore

    return div(*args, **kwargs)
