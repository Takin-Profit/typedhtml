# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class menu_props(ui5_tag_props, total=False):
    header_text: str
    busy: bool
    busy_delay: int
    open_: bool
    opener: str


class menu(ui5_tag):
    """ui5-menu component represents a hierarchical menu structure."""

    def __init__(self, *args, **kwargs: Unpack[menu_props]) -> None:
        self.tagname = "ui5-menu"
        super().__init__(*args, **kwargs)


class menu_item_props(ui5_tag_props, total=False):
    accessible_name: str
    additional_text: str
    busy: bool
    busy_delay: int
    disabled: bool
    icon: str
    starts_section: bool
    text: str


class menu_item(ui5_tag):
    """ui5-menu-item component represents a choice in a menu. The ui5-menu-item
    is a clickable element which opens a menu on click. The content inside the
    ui5-menu-item defines the text of the item. The items inside the menu
    should be provided as standard HTML elements."""

    def __init__(self, *args, **kwargs: Unpack[menu_item_props]) -> None:
        self.tagname = "ui5-menu-item"
        super().__init__(*args, **kwargs)
