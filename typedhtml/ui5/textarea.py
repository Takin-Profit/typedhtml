# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class textarea_props(ui5_tag_props, total=False):
    placeholder: str
    accessible_name: str
    accessible_name_ref: str
    disabled: bool
    growing: bool
    growing_max_lines: int
    maxlength: int
    name: str
    readonly: bool
    required: bool
    rows: int
    show_exceeded_text: bool
    value: str
    value_state: Literal["None", "Error", "Warning", "Success", "Information"]


class textarea(ui5_tag):
    """The ui5-textarea component is used to enter multiple lines of text."""

    def __init__(self, *args, **kwargs: Unpack[textarea_props]) -> None:
        self.tagname = "ui5-textarea"
        super().__init__(*args, **kwargs)
