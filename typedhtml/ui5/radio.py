# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class radio_props(ui5_tag_props, total=False):
    name: str
    accessible_name: str
    accessible_name_ref: str
    checked: bool
    disabled: bool
    readonly: bool
    required: bool
    text: str
    value: str
    value_state: Literal["None", "Success", "Error", "Information", "Warning"]
    wrapping_type: Literal["None", "Normal"]


class radio_button(ui5_tag):
    """The ui5-radio component enables users to select a single option from a set
    of options.
    When a ui5-radio element is selected by the user, the select event is fired.
    When a ui5-radio element that is within a group is selected, the one that
    was previously selected gets automatically deselected. You can group radio buttons
    by using the name property."""

    def __init__(self, *args, **kwargs: Unpack[radio_props]):
        self.tagname = "ui5-radio-button"
        super().__init__(*args, **kwargs)
