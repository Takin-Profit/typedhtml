# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class multi_input_props(ui5_tag_props):
    value: str
    type: Literal["Text", "Email", "Tel", "Number", "Password", "Url"]
    value_state: Literal["None", "Success", "Warning", "Error", "Information"]
    icon: str
    value_state_message: str
    show_value_help_icon: bool


class multi_input(ui5_tag):
    """A ui5-multi-input field allows the user to enter multiple values, which
    are displayed as ui5-token."""

    def __init__(self, *args, **kwargs: Unpack[multi_input_props]) -> None:
        self.tagname = "ui5-multi-input"
        super().__init__(*args, **kwargs)


class token_props(ui5_tag_props):
    readonly: bool
    selected: bool
    text: str


class token(ui5_tag):
    """The ui5-token represents a short piece of information, such as objects,
    contacts, or actions in a compact form."""

    def __init__(self, *args, **kwargs: Unpack[token_props]) -> None:
        self.tagname = "ui5-token"
        super().__init__(*args, **kwargs)
