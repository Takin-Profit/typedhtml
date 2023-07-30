# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div
from typedhtml.uikit.types import Heading

from .util import add_val, heading


def card(*args: Any, body: bool = True, **kwargs: Unpack[GLOBAL_ATTR]) -> div:
    """Create layout boxes with different styles.

    see: `https://getuikit.com/docs/card`
    """
    add_val("cls", f"uk-card {'uk-card-body' if body else ''}", kwargs)  # type: ignore
    return div(*args, **kwargs)


def card_title(
    *args: Any,
    text: str,
    heading_size: Heading = "h3",
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """Create layout boxes with different styles.

    see: `https://getuikit.com/docs/card`
    """
    add_val("cls", "uk-card-title", kwargs)  # type: ignore
    d = div(*args, **kwargs)
    with d:
        heading(heading_size, text)
    return d
