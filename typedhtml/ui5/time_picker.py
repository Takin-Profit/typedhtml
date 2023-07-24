# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class time_picker_props(ui5_tag_props, total=False):
    date_value: str
    format_pattern: str
    place_holder: str


class time_picker(ui5_tag):
    """The ui5-time-picker component provides an input field with assigned clocks
    which opens on user action."""

    def __init__(self, *args, **kwargs: Unpack[time_picker_props]) -> None:
        self.tagname = "ui5-time-picker"
        super().__init__(*args, **kwargs)
