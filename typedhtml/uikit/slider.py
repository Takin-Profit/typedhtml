# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div
from typedhtml.uikit.util import add_val


def slider(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> div:
    """Create a responsive carousel slider.

    see: `https://getuikit.com/docs/slider`
    """
    add_val("uk-slider", "", kwargs)  # type: ignore
    return div(*args, **kwargs)


def slider_item(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> div:
    """Create a responsive carousel slider.

    see: `https://getuikit.com/docs/slider`
    """
    add_val("cls", "uk-slider-item", kwargs)  # type: ignore
    return div(*args, **kwargs)
