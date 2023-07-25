# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class side_nav_props(ui5_tag_props, total=False):
    collapsed: bool


class side_nav(ui5_tag):
    """The SideNavigation is used as a standard menu in applications. It consists
    of three containers: header (top-aligned), main navigation section (top-aligned)
    and the secondary section (bottom-aligned)."""

    def __init__(self, *args, **kwargs: Unpack[side_nav_props]):
        self.tagname = "ui5-side-navigation"
        super().__init__(*args, **kwargs)


class side_nav_item_props(ui5_tag_props, total=False):
    expanded: bool
    icon: str
    selected: bool
    whole_item_toggleable: bool
    text: str


class side_nav_item(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[side_nav_item_props]):
        self.tagname = "ui5-side-navigation-item"
        super().__init__(*args, **kwargs)


class side_nav_sub_item_props(ui5_tag_props, total=False):
    icon: str
    selected: bool
    text: str


class side_nav_sub_item(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[side_nav_sub_item_props]):
        self.tagname = "ui5-side-navigation-sub-item"
        super().__init__(*args, **kwargs)
