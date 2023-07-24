# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class tab_container_props(ui5_tag_props, total=False):
    collapsed: bool
    content_background_design: Literal["Solid", "Translucent", "Transparent"]
    fixed: bool
    header_background_design: Literal["Solid", "Translucent", "Transparent"]
    show_overflow: bool
    tab_layout: Literal["Inline", "Standard"]
    tabs_overflow_mode: Literal["End", "StartAndEnd"]


class tab_container(ui5_tag):
    """The ui5-tabcontainer represents a collection of tabs with associated content.
    Navigation through the tabs changes the content display of the currently active
    content area. A tab can be labeled with text only, or icons with text."""

    def __init__(self, *args, **kwargs: Unpack[tab_container_props]):
        self.tagname = "ui5-tabcontainer"
        super().__init__(*args, **kwargs)
