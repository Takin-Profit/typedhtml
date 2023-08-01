# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Any, Unpack

from typedhtml.attributes import a_attr
from typedhtml.tags import a
from typedhtml.uikit.types import LinkMods
from typedhtml.uikit.util import add_val


def link(
    *args: Any,
    classes: list[LinkMods],
    **kwargs: Unpack[a_attr],
) -> a:
    """Define different styles to integrate links into specific content.

    see: `https://getuikit.com/docs/link`_
    """
    add_val("cls", " ".join(classes), kwargs)  # type: ignore
    return a(*args, **kwargs)
