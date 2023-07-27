# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Self, TypedDict, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import typed_tag


class ui5_tag_props(GLOBAL_ATTR, total=False):
    slot: str


class ui5_tag(typed_tag):
    """Base class for all UI5 Web Components."""

    def __init__(self: Self, *args, **kwargs: Unpack[ui5_tag_props]) -> None:
        super().__init__(*args, **kwargs)


class AccessibilityAttributes(TypedDict, total=False):
    expanded: bool
    has_popup: Literal["Dialog", "Grid", "Listbox", "Menu", "Tree"]
