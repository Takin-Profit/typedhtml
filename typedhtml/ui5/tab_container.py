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


class tab_props(ui5_tag_props, total=False):
    design: Literal["Default", "Neutral", "Positive", "Critical", "Negative"]
    disabled: bool
    icon: str
    selected: bool
    text: str


class tab(ui5_tag):
    """The ui5-tab represents a selectable item inside a ui5-tabcontainer.
    It defines both the item in the tab strip (top part of the control) and the
    content that is presented to the user once the tab is selected."""

    def __init__(self, *args, **kwargs: Unpack[tab_props]):
        self.tagname = "ui5-tab"
        super().__init__(*args, **kwargs)


class tab_separator(ui5_tag):
    """The ui5-tab-separator represents a vertical line to separate tabs inside a
    ui5-tabcontainer. It can be used as a visual aid, e.g. to separate tabs with
    different types of content."""

    def __init__(self, *args, **kwargs):
        self.tagname = "ui5-tab-separator"
        super().__init__(*args, **kwargs)
