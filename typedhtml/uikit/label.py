# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import span
from typedhtml.uikit.util import add_val


def label(
    *args: Any,
    kind: Literal["success", "warning", "danger"],
    **kwargs: Unpack[GLOBAL_ATTR],
) -> span:
    """Indicate important notes and highlight parts of your content.
    see: `https://getuikit.com/docs/label`_
    """

    add_val("cls", f"uk-label uk-label-{kind}", kwargs)  # type: ignore
    return span(*args, **kwargs)
