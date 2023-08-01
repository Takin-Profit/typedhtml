# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.attributes import a_attr
from typedhtml.tags import a
from typedhtml.uikit.util import add_val


def marker(*args: Any, **kwargs: Unpack[a_attr]) -> a:
    """Create a marker icon that can be displayed on top of images."""

    add_val("uk-marker", "", kwargs)  # type: ignore
    return a(*args, **kwargs)
