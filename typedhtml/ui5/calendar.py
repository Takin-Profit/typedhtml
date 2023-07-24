# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal, Self, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class calendar_props(ui5_tag_props, total=False):
    hide_week_numbers: bool
    selection_mode: Literal["Single", "Range", "Multiple"]


class calendar(ui5_tag):
    """The ui5-calendar component allows users to select one or more dates.

    Currently selected dates are represented with instances of ui5-date as children
    of the ui5-calendar. The value property of each ui5-date must be a date string,
    correctly formatted according to the ui5-calendar's formatPattern property. Whenever
    the user changes the date selection, ui5-calendar will automatically create/remove
    instances of ui5-date in itself, unless you prevent this behavior by calling
    preventDefault() for the selected-dates-change event. This is useful if you want to
    control the selected dates externally."""

    def __init__(self: Self, *args, **kwargs: Unpack[calendar_props]) -> None:
        self.tagname = "ui5-calendar"
        super().__init__(*args, **kwargs)
