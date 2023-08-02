# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div
from typedhtml.uikit.util import add_val


def placeholder(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> div:
    """Create a placeholder space that can be used for uploading files
    via drag and drop.

    see: `https://getuikit.com/docs/placeholder`
    """
    add_val("cls", "uk-placeholder", kwargs)  # type: ignore
    return div(*args, **kwargs)
