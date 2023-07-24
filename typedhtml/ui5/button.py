# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import AccessibilityAttributes, ui5_tag, ui5_tag_props


class button_props(ui5_tag_props, total=False):
    accessibility_attributes: AccessibilityAttributes
    accessible_name: str
    accessible_name_ref: str
    design: Literal["Default", "Emphasized", "Positive", "Negative", "Transparent"]
    design: Literal["Default", "Emphasized", "Positive", "Negative", "Transparent"]

    icon: str
    icon_end: bool
    submits: bool
    tooltip: str
    type: Literal["Button", "Submit", "Reset"]


class button(ui5_tag):
    """The ui5-button component represents a simple push button.
    It enables users to trigger actions by clicking or tapping the ui5-button,
    or by pressing certain keyboard keys, such as Enter."""

    def __init__(self, *args, **kwargs: Unpack[button_props]) -> None:
        self.tagname = "ui5-button"
        super().__init__(*args, **kwargs)
