# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class popover_props(ui5_tag_props):
    header_text: str
    allow_target_overlap: bool
    hide_arrow: bool
    hide_backdrop: bool
    horizontalAlign: Literal["Center", "Left", "Right", "Stretch"]
    modal: bool
    opener: str
    placement_type: Literal["Bottom", "Top", "Left", "Right"]
    vertical_align: Literal["Center", "Top", "Bottom", "Stretch"]


class popover(ui5_tag):
    """The ui5-popover component displays additional information for an object in a
    compact way and without leaving the page. The Popover can contain various UI
    elements, such as fields, tables, images, and charts. It can also include actions
    in the footer."""

    def __ini__(self, *args, **kwargs: Unpack[popover_props]):
        self.tagname = "ui5-popover"
        super().__init__(*args, **kwargs)
