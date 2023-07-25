# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class shell_bar_props(ui5_tag_props, total=False):
    primary_title: str
    secondary_title: str
    accessibility_attributes: dict[str, str]
    accessibility_rules: dict[str, str]
    accessibility_texts: dict[str, str]
    notifications_count: str
    show_co_pilot: bool
    show_notifications: bool
    show_product_switch: bool
    show_search_field: bool


class shell_bar(ui5_tag):
    """The ui5-shellbar is meant to serve as an application header and includes
    numerous built-in features, such as: logo, profile image/icon, title,
    search field, notifications and so on."""

    def __init__(self, *args, **kwargs: Unpack[shell_bar_props]):
        self.tagname = "ui5-shellbar"
        super().__init__(*args, **kwargs)


class shell_bar_item_props(ui5_tag_props, total=False):
    count: str
    icon: str
    text: str


class shell_bar_item(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[shell_bar_item_props]):
        self.tagname = "ui5-shellbar-item"
        super().__init__(*args, **kwargs)
