# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div
from typedhtml.uikit.util import add_val


def spinner(
    args: Any, ratio: Optional[int] = None, **kwargs: Unpack[GLOBAL_ATTR]
) -> div:
    """Create an animated loading spinner.

    see: `https://getuikit.com/docs/spinner`_
    """
    _ratio = f"ratio: {ratio};" if ratio else ""
    add_val("uk-spinner", _ratio, kwargs)  # type: ignore
    return div(*args, **kwargs)
