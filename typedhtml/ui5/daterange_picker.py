# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class daterange_picker_props(ui5_tag_props, total=False):
    date_value: str
    date_value_utc: str
    delimiter: str
    end_date_value: str
    start_date_value: str
    format_pattern: str


class daterange_picker(ui5_tag):
    """The DateRangePicker enables the users to enter a localized date range using
    touch, mouse, keyboard input, or by selecting a date range in the calendar."""

    def __init__(self, *args, **kwargs: Unpack[daterange_picker_props]):
        self.tagname = "ui5-daterange-picker"
        super().__init__(*args, **kwargs)
