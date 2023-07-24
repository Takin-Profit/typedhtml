# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class datepicker_props(ui5_tag_props, total=False):
    value: str
    accessible_name: str
    accessible_name_ref: str
    date_value: str
    disabled: bool
    hide_week_numbers: bool
    name: str
    placeholder: str
    readonly: bool
    required: bool
    value_state: Literal["Warning", "Error", "Success", "Information", "None"]


class date_picker(ui5_tag):
    """The ui5-date-picker component provides an input field with assigned calendar
    which opens on user action. The ui5-date-picker allows users to select a localized
    date using touch, mouse, or keyboard input. It consists of two parts: the date input
    field and the date picker."""

    def __init__(self, *args, **kwargs: Unpack[datepicker_props]):
        self.tagname = "ui5-date-picker"
        super().__init__(*args, **kwargs)
