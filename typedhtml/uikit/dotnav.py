# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Any, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import ul
from typedhtml.uikit.util import add_val


def dotnav(*args: Any, is_vertical: bool, **kwargs: Unpack[GLOBAL_ATTR]) -> ul:
    """Create a dot navigation to operate slideshows or to scroll to different page
    sections.

    see: `https://getuikit.com/docs/dotnav`_
    """

    add_val("cls", "uk-dotnav", kwargs)  # type: ignore
    if is_vertical:
        add_val("cls", "uk-dotnav-vertical", kwargs)  # type: ignore

    return ul(*args, **kwargs)
