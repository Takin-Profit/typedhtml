# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import hr
from typedhtml.uikit.util import add_val


def divider(
    *args: Any, is_small: bool, is_vertical: bool, **kwargs: Unpack[GLOBAL_ATTR]
) -> hr:
    """Create a divider to separate content.

    see: `https://getuikit.com/docs/divider`_
    """
    if not is_small and not is_vertical:
        add_val("cls", "uk-divider-icon", kwargs)  # type: ignore
    if is_small:
        add_val("cls", "uk-divider-small", kwargs)  # type: ignore
    if is_vertical:
        add_val("cls", "uk-divider-vertical", kwargs)  # type: ignore

    return hr(*args, **kwargs)
