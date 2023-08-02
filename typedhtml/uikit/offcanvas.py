# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import button, div
from typedhtml.uikit.util import add_val

Animation = Literal["slide", "push", "reveal", "none"]


def offcanvas(
    *args: Any,
    close: bool = True,
    animation: Animation = "slide",
    overlay: bool = False,
    flip: bool = False,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """Create an off-canvas sidebar that slides in and out of the page, which is perfect
    for creating mobile navigations.

    see: `https://getuikit.com/docs/offcanvas`
    """
    _flip = " flip: true;" if flip else ""
    _overlay = " overlay: true;" if overlay else ""
    _ani = f" animation: {animation};"
    add_val("uk-offcanvas", f"{_overlay}{_flip}{_ani}", kwargs)  # type: ignore

    off = div(*args, **kwargs)

    if close:
        off.add(button(cls="uk-offcanvas-close", type_="button", uk_close=""))  # type: ignore

    return off
