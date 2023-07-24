# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal, Self, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class checkbox_props(ui5_tag_props, total=False):
    checked: bool
    disabled: bool
    name: str
    readonly: bool
    text: str
    value: str
    accessible_name: str
    accessible_name_ref: str
    indeterminate: bool
    required: bool
    value_state: Literal["Warning", "Error", "Success", "Information", "None"]
    value_state: Literal["Warning", "Error", "Success", "Information", "None"]
    wrapping_type: Literal["None", "Normal"]


class checkbox(ui5_tag):
    """
        Allows the user to set a binary value, such as true/false or yes/no for an item.

    The ui5-checkbox component consists of a box and a label that describes its purpose.
    If it's checked, an indicator is displayed inside the box. To check/uncheck the
    ui5-checkbox,
    the user has to click or tap the square box or its label.

    The ui5-checkbox component only has 2 states - checked and unchecked.
    Clicking or tapping toggles the ui5-checkbox between checked and unchecked state."""

    def __init__(self: Self, *args, **kwargs: Unpack[checkbox_props]) -> None:
        self.tagname = "ui5-checkbox"
        super().__init__(*args, **kwargs)
