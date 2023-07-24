# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class rating_indicator_props(ui5_tag_props, total=False):
    value: int
    accessible_name: str
    accessible_name_ref: str
    disabled: bool
    max_: int
    readonly: bool
    required: bool


class rating_indicator(ui5_tag):
    """<ui5-rating-indicator> The Rating Indicator is used to display a specific number
    of icons that are used to rate an item. Additionally, it is also used to display
    the average and overall ratings."""

    def __init__(self, *args, **kwargs: Unpack[rating_indicator_props]):
        self.tagname = "ui5-rating-indicator"
        super().__init__(*args, **kwargs)
