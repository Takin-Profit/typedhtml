# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class combobox_props(ui5_tag_props):
    placeholder: str
    accessible_name: str
    accessible_name_ref: str
    disabled: bool
    filter: Literal["StartsWithPerTerm", "StartsWith", "Contains", "None"]
    loading: bool
    readonly: bool
    required: bool
    value: str
    value_state: Literal["Warning", "Error", "Success", "Information", "None"]


class combobox(ui5_tag):
    """The ui5-combobox component represents a drop-down menu with a list of the
    available options and a text input field to narrow down the options.

    It is commonly used to enable users to select an option from a predefined list."""

    def __init__(self, *args, **kwargs: Unpack[combobox_props]):
        self.tagname = "ui5-combobox"
        super().__init__(*args, **kwargs)
