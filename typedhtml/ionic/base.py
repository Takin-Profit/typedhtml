# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Self, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import typed_tag


class ion_tag_props(GLOBAL_ATTR, total=False):
    mode: Literal["ios", "md"]


class ion_tag(typed_tag):
    """Base class for all UI5 Web Components."""

    def __init__(self: Self, *args: Any, **kwargs: Unpack[ion_tag_props]) -> None:
        super().__init__(*args, **kwargs)


Color = Literal[
    "primary",
    "secondary",
    "tertiary",
    "success",
    "warning",
    "danger",
    "light",
    "medium",
    "dark",
]

Target = Literal["_blank", "_parent", "_self", "_top"]
