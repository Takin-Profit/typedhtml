# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class link_props(ui5_tag_props, total=False):
    accessibility_attributes: str
    accessible_name: str
    accessible_name_ref: str
    accessible_role: str
    design: Literal["Default", "Subtle", "Emphasized"]
    disabled: bool
    wrapping_type: Literal["Normal", "None"]


class link(ui5_tag):
    """The Link component allows the user to navigate to another resource or
    to trigger an action. It is clickable and can hold arbitrary content."""

    def __init__(self, *args, **kwargs: Unpack[link_props]) -> None:
        self.tagname = "ui5-link"
        super().__init__(*args, **kwargs)
