# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div
from typedhtml.uikit.types import Container
from typedhtml.uikit.util import add_val


def container(
    *args: Any, size: Optional[Container] = None, **kwargs: Unpack[GLOBAL_ATTR]
) -> div:
    """The Container component is a simple wrapper for your site content.

    see: `https://getuikit.com/docs/container`_
    """

    add_val("cls", f"uk-container {size or ''}", kwargs)  # type: ignore

    return div(*args, **kwargs)
