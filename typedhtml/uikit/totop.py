# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.attributes import a_attr
from typedhtml.tags import a


def totop(*args: Any, **kwargs: Unpack[a_attr]) -> a:
    """Create a simple to-top scroller."""

    return a(*args, href="#", uk_totop="", **kwargs)  # type: ignore
