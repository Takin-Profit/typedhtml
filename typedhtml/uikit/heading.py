# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.uikit.types import HeadingType

from .types import Heading as H
from .util import add_val
from .util import heading as h

Size = Literal["small", "large", "medium", "xlarge", "2xlarge"]


def heading(
    *args: Any,
    size: Size,
    h_size: H,
    divider: bool = False,
    line: bool = False,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> HeadingType:
    """_summary_

    Args:
        size (Size): the uikit size class modifier
        h_size (H): the actual heading size (h1, h2, etc)

    Returns:
        Combine this component with the Text component to style your headings.
        see: `https://getuikit.com/docs/heading`
    """
    _div = " uk-heading-divider" if divider else ""
    _line = " uk-heading-line" if line else ""
    add_val("cls", f"uk-heading-{size}{_div}{_line}", kwargs)  # type: ignore
    kwargs.pop("size", None)  # type: ignore
    return h(*args, size=h_size, **kwargs)
