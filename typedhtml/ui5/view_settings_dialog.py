# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class view_settings_dialog_props(ui5_tag_props, total=False):
    sort_descending: bool


class view_settings_dialog(ui5_tag):
    """The ui5-view-settings-dialog component helps the user to sort data within a
    list or a table. It consists of several lists like Sort order which is built-in
    and Sort By and Filter By lists, for which you must be provide items(ui5-sort-item
    & ui5-filter-item respectively) These options can be used to create sorters
    for a table."""

    def __init__(self, *args, **kwargs):
        self.tagname = "ui5-view-settings-dialog"
        super().__init__(*args, *kwargs)


class sort_item_props(ui5_tag_props, total=False):
    selected: bool
    text: str


class sort_item(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[sort_item_props]):
        self.tagname = "ui5-sort-item"
        super().__init__(*args, **kwargs)


class filter_item_props(ui5_tag_props, total=False):
    additional_text: str
    text: str


class filter_item(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[filter_item_props]):
        self.tagname = "ui5-filter-item"
        super().__init__(*args, **kwargs)


class filter_item_option_props(ui5_tag_props, total=False):
    selected: bool
    text: str


class filter_item_option(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[filter_item_option_props]):
        self.tagname = "ui5-filter-item-option"
        super().__init__(*args, **kwargs)
