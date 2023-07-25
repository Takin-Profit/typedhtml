# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class flexible_column_layout_props(ui5_tag_props, total=False):
    accessibility_roles: str
    accessibility_texts: str
    end_columns_visible: bool
    hide_arrows: bool
    layout: Literal[
        "OneColumn",
        "TwoColumnsStartExpanded",
        "TwoColumnsMidExpanded",
        "ThreeColumnsMidExpanded",
        "ThreeColumnsEndExpanded",
        "ThreeColumnsStartExpandedEndHidden",
        "ThreeColumnsMidExpandedEndHidden",
        "MidColumnFullScreen",
        "EndColumnFullScreen",
    ]
    mid_column_visible: bool
    start_column_visible: bool
    visible_columns: int


class flexible_column_layout(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[flexible_column_layout_props]) -> None:
        self.tagname = "ui5-flexible-column-layout"
        super().__init__(*args, **kwargs)
