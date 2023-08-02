# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div
from typedhtml.uikit.util import add_val

Style = Literal["default", "muted", "primary", "secondary"]
Size = Literal[
    "small",
    "large",
    "xsmall",
    "xlarge",
    "padding-remove-vertical",
]


def section(
    *args: Any,
    style_: Style = "default",
    preserve_color: bool = False,
    overlap: bool = False,
    size_: Optional[Size] = None,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """Create a section with a background image.

    see: `https://getuikit.com/docs/section`
    """
    style = f" uk-section-{style_}"
    preserve = " uk-preserve-color" if preserve_color else ""
    size = f" uk-section-{size_}" if size_ else ""
    overlap_ = " uk-section-overlap" if overlap else ""
    add_val("cls", f"uk-section{style}{preserve}{size}{overlap_}", kwargs)  # type: ignore
    return div(*args, **kwargs)
