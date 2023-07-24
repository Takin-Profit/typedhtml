# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class step_input_props(ui5_tag_props, total=False):
    value: int
    accessible_name: str
    accessible_name_ref: str
    disabled: bool
    max_: int
    min_: int
    name: str
    placeholder: str
    readonly: bool
    required: bool
    step: int
    value_precision: int
    value_state: Literal["None", "Success", "Warning", "Error", "Information"]


class step_input(ui5_tag):
    """The ui5-step-input consists of an input field and buttons with icons to
    increase/decrease the value with the predefined step."""

    def __init__(self, *args, **kwargs: Unpack[step_input_props]):
        self.tagname = "ui5-step-input"
        super().__init__(*args, **kwargs)
