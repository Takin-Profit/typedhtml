# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class segmented_button_props(ui5_tag_props, total=False):
    accessible_name: str
    mode: Literal["SingleSelect", "MultiSelect"]
    selected_item: str


class segmented_button(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[segmented_button_props]):
        self.tagname = "ui5-segmented-button"
        super().__init__(*args, **kwargs)


class segmented_button_item_props(ui5_tag_props, total=False):
    design: str
    icon_end: bool
    submits: bool


class segmented_button_item(ui5_tag):
    """<ui5-segmented-button> The ui5-segmented-button shows a group of items.
    When the user clicks or taps one of the items, it stays in a pressed state.
    It automatically resizes the items to fit proportionally within the component.
    When no width is set, the component uses the available width."""

    def __init__(self, *args, **kwargs: Unpack[segmented_button_item_props]):
        self.tagname = "ui5-segmented-button-item"
        super().__init__(*args, **kwargs)
