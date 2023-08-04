# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import h1, h2, h3, h4, h5, h6
from typedhtml.uikit.types import HeadingType

from .types import Heading as H
from .util import add_val

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
    match h_size:
        case "h1":
            return h1(*args, **kwargs)
        case "h2":
            return h2(*args, **kwargs)
        case "h3":
            return h3(*args, **kwargs)
        case "h4":
            return h4(*args, **kwargs)
        case "h5":
            return h5(*args, **kwargs)
        case "h6":
            return h6(*args, **kwargs)
