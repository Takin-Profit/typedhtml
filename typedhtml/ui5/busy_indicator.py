# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class busy_indicator_props(ui5_tag_props, total=False):
    size: Literal["Small", "Medium", "Large"]
    active: bool
    delay: int
    text: str


class busy_indicator(ui5_tag):
    """Displays an animated circular symbol indicating that an operation is ongoing.
    You can change the size of the `BusyIndicator` with the `size` property or set your
    custom CSS size class."""

    def __init__(self, *args, **kwargs: Unpack[busy_indicator_props]) -> None:
        self.tagname = "ui5-busy-indicator"
        super().__init__(*args, **kwargs)
