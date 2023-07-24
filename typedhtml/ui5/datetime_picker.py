# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from typing import Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class datetime_picker(ui5_tag):
    """The DateTimePicker component allows users to select both date
    (day, month and year)
    and time (hours, minutes and seconds) and for the purpose it consists of input field
    and Date/Time picker."""

    def __init__(self, *args, **kwargs: Unpack[ui5_tag_props]):
        self.tagname = "ui5-datetime-picker"
        super().__init__(*args, **kwargs)
