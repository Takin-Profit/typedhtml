# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.attributes import a_attr
from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import a, div
from typedhtml.uikit.util import add_val


def scroll(*args: Any, **kwargs: Unpack[a_attr]) -> a:
    """Scroll smoothly when jumping to different sections on a page.

    see: `https://getuikit.com/docs/scroll`
    """
    add_val("cls", "uk-scroll", kwargs)  # type: ignore
    return a(*args, **kwargs)


def scrollspy(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> div:
    """Trigger events and animations while scrolling your page."""

    add_val("uk-scrollspy", True, kwargs)  # type: ignore
    return div(*args, **kwargs)
