# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Any, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import a, div
from typedhtml.uikit.base import Style
from typedhtml.uikit.util import add_val


def alert(
    animation: bool = False,
    duration: int = 0,
    style: Style = "primary",
    *args: Any,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """Display success, warning and error messages.
    see: `https://getuikit.com/docs/alert`_
    """
    opts: list[str] = []
    if animation:
        opts.append("animation: true;")
    if duration > 0:
        opts.append(f"duration: {duration};")

    add_val("cls", f"uk-alert-{style}", kwargs)  # type: ignore
    add_val("uk-alert", " ".join(opts), kwargs)  # type: ignore
    it = div(*args, **kwargs)
    with it:
        a(cls="uk-alert-close", uk_close="")  # type: ignore
    return it
