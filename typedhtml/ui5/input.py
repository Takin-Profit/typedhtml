# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class input_props(ui5_tag_props):
    show_clear_icon: bool
    value: str
    accessible_name: str
    accessible_name_ref: str
    disabled: bool
    max_length: int
    name: str
    no_typeahead: bool
    placeholder: str
    preview_item: str
    readonly: bool
    required: bool
    show_suggestions: bool
    type: Literal["Text", "Number", "Password", "Tel", "Email", "Url"]
    value_state: Literal["None", "Success", "Warning", "Error", "Information"]


class input(ui5_tag):
    """The ui5-input component allows the user to enter and edit text or numeric values
        in one line.
    Additionally, you can provide suggestionItems,
    that are displayed in a popover right under the input."""

    def __init__(self, *args, **kwargs: Unpack[input_props]) -> None:
        self.tagname = "ui5-input"
        super().__init__(*args, **kwargs)
