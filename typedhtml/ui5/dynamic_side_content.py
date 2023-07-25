# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class dynamic_side_content_props(ui5_tag_props, total=False):
    equal_split: bool
    hide_main_content: bool
    hide_side_content: bool
    side_content_fall_down: Literal["BelowXL", "BelowL", "BelowM", "OnMinimumWidth"]
    side_content_position: Literal["End", "Start"]
    side_content_visibility: Literal[
        "AlwaysShow",
        "ShowAboveL",
        "ShowAboveM",
        "ShowAboveS",
        "NeverShow",
    ]


class dynamic_side_content(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[dynamic_side_content_props]) -> None:
        self.tagname = "ui5-dynamic-side-content"
        super().__init__("ui5-dynamic-side-content", *args, **kwargs)
