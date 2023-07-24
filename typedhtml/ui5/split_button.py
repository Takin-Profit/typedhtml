# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class split_button_props(ui5_tag_props, total=False):
    accessible_name: str
    active_icon: str
    design: Literal[
        "Default", "Emphasized", "Positive", "Negative", "Transparent", "Attention"
    ]
    disabled: bool
    icon: str


class split_button(ui5_tag):
    """<ui5-split-button> enables users to trigger actions. It is constructed of two
    separate actions - default action and arrow action that can be activated by
    clicking or tapping, or by pressing certain keyboard keys - Space or Enter for
    default action, and Arrow Down or Arrow Up for arrow action."""

    def __init__(self, *args, **kwargs: Unpack[split_button_props]):
        self.tagname = "ui5-split-button"
        super().__init__(*args, **kwargs)
