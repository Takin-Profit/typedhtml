# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import span
from typedhtml.uikit.util import add_val


def badge(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> span:
    """Badge is a small inline block that can be used to label something.

    see: `https://getuikit.com/docs/badge`
    """
    add_val("cls", "uk-badge", kwargs)  # type: ignore
    return span(*args, **kwargs)
