# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class multi_combobox_props(ui5_tag_props):
    placeholder: str
    accessible_name: str
    accessible_name_ref: str
    allow_custom_values: bool
    disabled: bool
    filter: Literal["StartsWithPerTerm", "StartsWith", "Contains", "None"]
    no_typeahead: bool
    open_: bool
    readonly: bool
    required: bool
    value: str
    value_state: Literal["None", "Success", "Warning", "Error", "Information"]


class multi_combobox(ui5_tag):
    """The ui5-multi-combobox component consists of a list box with items and a text
    field allowing the user to either type a value directly into the text field, or
    choose from the list of existing items."""

    def __init__(self, *args, **kwargs: Unpack[multi_combobox_props]) -> None:
        self.tagname = "ui5-multi-combobox"
        super().__init__(*args, **kwargs)


class multi_combobox_item_props(ui5_tag_props):
    selected: bool


class mcb_item(ui5_tag):
    """The ui5-multi-combobox-item represents the item for a ui5-multi-combobox.
    The ui5-multi-combobox-items are usually used in a suggestion list, where the
    user can select one or multiple items from. The items hold the data and are
    visualized as a list of text with icons or images."""

    def __init__(self, *args, **kwargs: Unpack[multi_combobox_item_props]) -> None:
        self.tagname = "ui5-mcb-item"
        super().__init__(*args, **kwargs)


class mcb_group_item_props(ui5_tag_props):
    text: str


class mcb_group_item(ui5_tag):
    """The ui5-multi-combobox-group-item represents a group in a ui5-multi-combobox.
    The ui5-multi-combobox-group-items are used to group ui5-multi-combobox-items
    together to show in the suggestion list."""

    def __init__(self, *args, **kwargs: Unpack[mcb_group_item_props]) -> None:
        self.tagname = "ui5-mcb-group-item"
        super().__init__(*args, **kwargs)
