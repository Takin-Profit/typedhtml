# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class select_props(ui5_tag_props, total=False):
    accessible_name: str
    accessible_name_ref: str
    disabled: bool
    name: str
    required: bool
    selected_option: str
    value_state: Literal["None", "Success", "Warning", "Error", "Information"]


class select(ui5_tag):
    """The ui5-select component is used to create a drop-down list. The items inside
    the ui5-select define the available options by using the ui5-option component."""

    def __init__(self, *args, **kwargs: Unpack[select_props]):
        self.tagname = "ui5-select"
        super().__init__(*args, **kwargs)


class option_props(ui5_tag_props, total=False):
    icon: str
    selected: bool
    additional_text: str
    value: str
    disabled: bool


class option(ui5_tag):
    """<ui5-option> Defines the content of an option in the <ui5-select> component.
    Note: When <ui5-option> is placed inside a <ui5-select>, it will be overwritten.
    """

    def __init__(self, *args, **kwargs: Unpack[option_props]):
        self.tagname = "ui5-option"
        super().__init__(*args, **kwargs)
